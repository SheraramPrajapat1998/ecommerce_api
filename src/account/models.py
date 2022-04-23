from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# utils
from account import utils

class User(AbstractUser):
    GENDER = (
        ('Male', _("MALE")),
        ('Female', _("FEMALE"))
    )

    TYPE = (
        ('buyer', _('Buyer')),
        ('seller', _('Seller')),
    )
    id = models.CharField(max_length=60,primary_key=True,unique=True,editable=False,default=utils.generate_uuid())
    username = models.CharField(max_length=256, unique=True)
    gender = models.TextField(choices=GENDER, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    mobile_no = models.CharField(
        unique=True, max_length=10, null=True, blank=True)
    profile_photo = models.ImageField(upload_to='Users/', null=True, blank=True)


    # @property
    # def 