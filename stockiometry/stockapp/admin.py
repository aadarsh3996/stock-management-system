from django.contrib import admin
from stockapp import models

# Register your models here.

admin.site.register(models.CompanyList)
admin.site.register(models.Order)
admin.site.register(models.Track)
