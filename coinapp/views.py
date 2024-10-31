from django.contrib.auth import get_user_model
from django.views.generic import CreateView, ListView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.db.models import Q, F, BooleanField, Case, When, Sum
from django.db import transaction
from django.contrib import messages
from django.urls import reverse_lazy
from coinapp.models import Transaction, Offering, UserOffering, GeneralSettings
from coinapp.forms import SignUpForm

User = get_user_model()


def about_view(request):
    GeneralSettings.objects.filter(key="about").update(value=F("value") + 1)
    return render(request, "about.html")


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("coinapp:home")
    template_name = "registration/signup.html"

def get_transactions(user):
    return (
        Transaction.objects.filter(Q(seller=user) | Q(buyer=user))
        .select_related("seller", "buyer")
        .annotate(
            is_received=Case(
                When(Q(seller=user), then=True),
                default=False,
                output_field=BooleanField(),
            )
        )
        .order_by("-created_at")
    )
@method_decorator(login_required, name="dispatch")
class HomeView(View):
    def get(self, request):
        users = User.objects.exclude(username=request.user.username)
        total = User.objects.aggregate(total=Sum("amount"))
        return render(
            request,
            "home.html",
            {"transactions": get_transactions(request.user), "users": users, "total": total},
        )

    def post(self, request):
        buyer = User.objects.get(username=request.POST["buyer"])
        seller = request.user
        amt = request.POST["amount"]
        if buyer == seller:
            messages.warning(request, "Error! Seller and buyer are same.")
        elif amt.isnumeric():

            description = request.POST["description"]
            with transaction.atomic():
                seller.amount = F("amount") + amt
                buyer.amount = F("amount") - amt
                seller.save()
                buyer.save()

                txn = Transaction.objects.create(
                    seller=seller, buyer=buyer, description=description, amount=amt
                )
                messages.success(request, f"Success! Payment success. txnId:{txn.id}")

        else:
            messages.warning(request, "Error! Amount must be a number.")
        return redirect("coinapp:home")


class UserList(ListView):
    paginate_by = 36
    template_name = "coinapp/user_list.html"
    context_object_name = "users"

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        queryset = User.objects.order_by("first_name")
        if query:
            queryset = queryset.filter(
                Q(username__icontains=query) | Q(first_name__icontains=query)
            )
        return queryset


class UserDetail(View):
    def get(self, request, **kwargs):
        user = User.objects.get(id=kwargs["user"])
        offerings = Offering.objects.order_by("-heading")
        userofferings = UserOffering.objects.select_related('offering').filter(user=user)
        return render(
            request,
            "coinapp/user_detail.html",
            {"user": user, "offerings": offerings,"transactions": get_transactions(user), "userofferings": userofferings},
        )

    @method_decorator(login_required)
    def post(self, request, **kwargs):
        if request.user.pk == kwargs["user"]:
            offering = Offering.objects.get(id=request.POST["offering"])
            my_offerings = request.user.offerings
            user_action = request.POST["action"]
            if user_action == "add":
                UserOffering.objects.update_or_create(
                    user=request.user,
                    offering=offering,
                    defaults={'rate':request.POST['rate']}
                )
                messages.success(request, f"Offering activated: {offering}.")            
            elif user_action == "remove":
                if my_offerings.count() < 2:
                    messages.warning(request, "Error: 1 offering is required..")
                else:
                    my_offerings.remove(offering)
                    messages.info(request, f"Offering deactivated: {offering}.")
            else:
                messages.warning(request, "Error: Invalid Action..")
        else:
            messages.warning(request, "Error: You can only create your offerings..")
        return redirect("coinapp:user_detail", user=kwargs["user"])


@login_required
def get_balance(request):
    user = User.objects.get(username=request.GET.get("username"))
    return HttpResponse(user.amount)
