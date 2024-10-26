from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    amount = models.IntegerField(default=0)

class Offering(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    heading = models.CharField(max_length=255)
    detail = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)

class Category(models.Model):
    heading = models.CharField(max_length=255)
    
class Transaction(models.Model):
    creator_person = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="txn_creator"
    )
    target_person = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="txn_target"
    )
    amount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

