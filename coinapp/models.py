from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    amount = models.IntegerField(default=0)
    offerings = models.ManyToManyField("Offering")

class Offering(models.Model):
    CAT_CHOICES = (
        ('Food', "Food"),
        ("Shelter","Shelter"),
        ("Clothing","Clothing"),
        ("Electronics","Electronics"),
        ("Water","Water"),
    )
    heading = models.CharField(max_length=255)
    detail = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)
    category = models.CharField(max_length=20,choices=CAT_CHOICES)

    def __str__(self):
        return f'{self.category} -> {self.heading}: ${self.amount}({self.detail[:30]}...)'


class Transaction(models.Model):
    creator_person = models.ForeignKey(
        "User", on_delete=models.PROTECT, related_name="txn_creator"
    )
    target_person = models.ForeignKey(
        "User", on_delete=models.PROTECT, related_name="txn_target"
    )
    offering = models.ForeignKey("Offering", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

