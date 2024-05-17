from django.db import models
from django.contrib.auth.models import Group
from core.entity.EntityCommon import EntityCommon

class Role(EntityCommon):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    entity = models.TextField(max_length=100, default= 'none')
    
    def concat_values_fields(self):
        self.concat_fields = f"{self.name},{self.description}"