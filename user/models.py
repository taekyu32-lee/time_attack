from email.headerregistry import AddressHeader
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"

    phone_number = models.CharField(max_length=255, default='')
    addr = models.CharField(max_length=255, default='')