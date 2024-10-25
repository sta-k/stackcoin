from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from django.contrib.auth import login
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.db.models import Q, F, BooleanField, Case, When, Sum

from django.contrib import messages

from coinapp.models import Transaction
from django.conf import settings

# Create your views here.
User = get_user_model()


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "last_name", "username", "password1", "password2")


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = "registration/signup_form.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home")


@method_decorator(login_required, name="dispatch")
class HomeView(View):
    template_name = "home.html"

    def get(self, request):
        transactions = (
            Transaction.objects.filter(
                Q(creator_person=request.user) | Q(target_person=request.user)
            )
            .select_related("creator_person", "target_person")
            .annotate(
                is_received=Case(
                    When(Q(creator_person=request.user), then=False),
                    default=True,
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
        touser = User.objects.get(username=request.POST["destAddress"])
        fromuser = request.user
        amount = int(request.POST["amount"]) * 100
        if touser == fromuser:
            messages.warning(
                request, "Error! You cannot send funds to your own account."
            )
        # elif fromuser.amount >= amount:
        else:
            touser.amount = F("amount") + amount
            fromuser.amount = F("amount") - amount
            touser.save()
            fromuser.save()
            txn = Transaction.objects.create(
                creator_person=fromuser, target_person=touser, amount=amount
            )
            messages.success(request, f"Success! Payment success. txnId:{txn.id}")
        # else:
        #     messages.warning(request, "Error! Low balance")
        return redirect("home")


# @login_required
# def getuser(request):
#     user = User.objects.get(username=request.GET["user"])
#     return HttpResponse(f"{user.first_name} {user.last_name}")
