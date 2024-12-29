from django.contrib.auth.models import AbstractUser
from django.db import models

class GeneralSettings(models.Model):
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=250)

    def __str__(self) -> str:
        return f'{self.key}:{self.value}'

class Exchange(models.Model):
    code  = models.CharField(max_length=5)
    title = models.CharField(max_length=255)
    address  = models.CharField(max_length=255)


class User(AbstractUser):
    exchange = models.ForeignKey("Exchange", on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)

class Category(models.Model):
    """
        Food
        Shelter
        Clothing
        Electronics
        Water
    """
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Listing(models.Model):   
    LISTING_CHOICES = [
        ('O', 'Offering'),
        ('W', 'Wants'),
    ] 
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    heading = models.CharField(max_length=255)
    detail = models.CharField(max_length=255)    
    rate = models.CharField(max_length=100, blank=True)
    listing_type = models.CharField(max_length=1, choices=LISTING_CHOICES)

    # is_active = models.BooleanField(default=True)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.heading}({self.detail[:30]}...)'
    
class Transaction(models.Model):
    seller = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="txn_seller"
    ) # creator
    buyer = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="txn_buer"
    ) # target
    description = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)
    # offering = models.ForeignKey("Offering", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.buyer} -> {self.seller}: {self.amount}"



