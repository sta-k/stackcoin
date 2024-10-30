from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.db.models import Q, F, BooleanField, Case, When, Sum
from django.db import transaction
from django.contrib import messages
from django.urls import reverse_lazy
from coinapp.models import Transaction, Offering
from coinapp.forms import SignUpForm

User = get_user_model()

from coinapp.models import GeneralSettings
def incr_counter(key):
    obj,created = GeneralSettings.objects.get_or_create(key=key)
    if created:
        obj.value = 1
    else:
        try:
            obj.value = int(obj.value) + 1
        except:
            obj.value=1
    obj.save()

def about_view(request):
    incr_counter('about')
    return render(request, "about.html")

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("coinapp:home")
    template_name = "registration/signup.html"

@method_decorator(login_required, name="dispatch")
class HomeView(View):
    def get(self, request):
        transactions = (
            Transaction.objects.filter(
                Q(seller=request.user) | Q(buyer=request.user)
            )
            .select_related("seller", "buyer")
            .annotate(
                is_received=Case(
                    When(Q(seller=request.user), then=True),
                    default=False,
                    output_field=BooleanField(),
                )
            )
            .order_by("-created_at")
        )
        users = User.objects.exclude(username=request.user.username)
        total = User.objects.aggregate(total=Sum("amount"))
        return render(
            request, "home.html", {"transactions": transactions, "users": users,"total": total}
        )

    def post(self, request):
        buyer = User.objects.get(username=request.POST["buyer"])
        seller = request.user
        amt = request.POST["amount"]
        if buyer == seller:
            messages.warning(
                request, "Error! Seller and buyer are same."
            )
        elif amt.isnumeric():
            
            description =  request.POST["description"]
            # amt = int()
            # offering = Offering.objects.get(id = request.POST["offering"])
            with transaction.atomic():
                seller.amount = F("amount") + amt
                buyer.amount = F("amount") - amt
                seller.save()
                buyer.save()
                
                txn = Transaction.objects.create(
                    seller=seller, buyer=buyer, description=description, amount = amt
                )
                messages.success(request, f"Success! Payment success. txnId:{txn.id}")
        
        else:
            messages.warning(
                request, "Error! Amount must be a number."
            )
        return redirect("coinapp:home")


@method_decorator(login_required, name="dispatch")
class OfferingView(View):
    def get(self, request):
        offering = Offering.objects.annotate(
            is_active=Case(
                When(Q(user=request.user), then=True),
                default=False,
                output_field=BooleanField(),
            )
        ).order_by('-is_active','category')
        return render(request, "coinapp/offerings.html",{"offerings":offering})
    def post(self, request):
        offering = Offering.objects.get(id = request.POST["offering"])
        is_active = request.POST.get('is_active')
        my_offerings = request.user.offerings
        if is_active:
            my_offerings.add(offering)
            messages.success(request, f"Offering activated: {offering}.")
        else:
            if my_offerings.count() < 2:
                messages.warning(request, "Error: At least 1 offering is required..")
            else:
                my_offerings.remove(offering)
                messages.info(request, f"Offering deactivated: {offering}.")
        return redirect("coinapp:offerings")
    
@login_required
def load_offerings(request):
    username = request.GET.get('username')
    offerings = []
    if username:
        offerings = Offering.objects.filter(user__username=username) # User.objects.get(username=username).offerings.all()
    return render(request, 'coinapp/user_offerings_list_options.html', {'offerings': offerings})


@login_required
def get_balance(request):
    user = User.objects.get(username=request.GET.get('username'))
    return HttpResponse(user.amount)