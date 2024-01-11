from collections.abc import Iterable
import os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext as _
from django.utils import timezone
from .manager import CustomUserManager
import uuid

def user_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.user.alias, filename)

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    email = models.EmailField(_("email address"), unique=True,)
    alias = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name",  "last_name"]

    def __str__(self):
        return self.email
    
    def save(self, *a, **b) -> None:
        self.alias = self.email.split('@')[0]
        return super().save(*a, **b)
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

STATES:dict[str] = {
                'FC' : 'Abuja',
                'AB' : 'Abia',
                'AD' : 'Adamawa',
                'AK' : 'Akwa Ibom',
                'AN' : 'Anambra',
                'BA' : 'Bauchi',
                'BY' : 'Bayelsa',
                'BE' : 'Benue',
                'BO' : 'Borno',
                'CR' : 'Cross River',
                'DE' : 'Delta',
                'EB' : 'Ebonyi',
                'ED' : 'Edo',
                'EK' : 'Ekiti',
                'EN' : 'Enugu',
                'GO' : 'Gombe',
                'IM' : 'Imo',
                'JI' : 'Jigawa',
                'KD' : 'Kaduna',
                'KN' : 'Kano',
                'KT' : 'Katsina',
                'KE' : 'Kebbi',
                'KO' : 'Kogi',
                'KW' : 'Kwara',
                'LA' : 'Lagos',
                'NA' : 'Nassarawa',
                'NI' : 'Niger',
                'OG' : 'Ogun',
                'ON' : 'Ondo',
                'OS' : 'Osun',
                'OY' : 'Oyo',
                'PL' : 'Plateau',
                'RI' : 'Rivers',
                'SO' : 'Sokoto',
                'TA' : 'Taraba',
                'YO' : 'Yobe',
                'ZA' : 'Zamfara'
    }
class Profile(models.Model):
    user = models.OneToOneField(User, related_name="user_profile", on_delete=models.CASCADE, null=True)
    state = models.CharField(max_length=2, choices=STATES)
    street = models.CharField(max_length=60, null=True, blank=True)
    house_no = models.CharField(max_length=5, null=True, blank=True)
    profession = models.CharField(max_length=128)
    pic = models.ImageField(upload_to=user_directory_path, blank=True)
    desc = models.TextField(default="")

    def __str__(self):
        return f'{self.user.id}'