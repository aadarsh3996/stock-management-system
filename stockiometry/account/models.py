from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class UserProfileInfo(models.Model):


    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING)

    mobile_number = models.CharField(max_length=10)
