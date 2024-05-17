from django.db import models
from django.contrib.auth.models import User
from core.entity.EntityCommon import EntityCommon
from core.enum.concrect import GENDER_CHOICES, MARITAL_STATUS_CHOICES

# Create your models here.
class Person(EntityCommon):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.TextField(max_length=100)
    identityCardNumber = models.TextField(max_length=100, unique= True)
    gender = models.CharField(choices= GENDER_CHOICES, max_length=100)
    maritalStatus = models.CharField(choices= MARITAL_STATUS_CHOICES, max_length=100)
    birthday = models.DateField()

    def concat_values_fields(self):
        self.concat_fields = f"{self.fullname},{self.identityCardNumber},{self.gender},{self.maritalStatus},{self.birthday}"