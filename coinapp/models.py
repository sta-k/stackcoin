from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    amount = models.IntegerField(default=0)

class Transaction(models.Model):
    input = models.ForeignKey("User", on_delete=models.CASCADE, related_name='txn_send')
    output = models.ForeignKey("User", on_delete=models.CASCADE, related_name='txn_recieved')
    output_amount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)