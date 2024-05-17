from django.db import models
from django.contrib.auth.models import Permission
from core.entity.EntityCommon import EntityCommon

class Privilege(EntityCommon):
    permission = models.OneToOneField(Permission, on_delete=models.CASCADE)
    entity = models.TextField(max_length=100, default= 'none')

    def concat_values_fields(self):
        self.concat_fields = f"{self.name},{self.description}"