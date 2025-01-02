from django.contrib import admin
from .models import Listing, GeneralSettings, Transaction

# Register your models here.
admin.site.register(Listing)
admin.site.register(GeneralSettings)
admin.site.register(Transaction)
