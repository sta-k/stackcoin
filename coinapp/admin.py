from django.contrib import admin
from .models import Offering, GeneralSettings, Transaction

# Register your models here.
admin.site.register(Offering)
admin.site.register(GeneralSettings)
admin.site.register(Transaction)
