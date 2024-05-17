import uuid
from django.db import models
from django.utils import timezone

class EntityCommon(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.UUIDField(null=True)

    updated_at = models.DateTimeField(default=timezone.now)
    updated_by = models.UUIDField(null=True)

    deleted_at = models.DateTimeField(null=True)
    deleted_by = models.UUIDField(null=True)

    concat_fields = models.TextField(unique=True)

    class Meta:
        abstract = True

    def concat_values_fields(self):
        self.concat_fields = f"{self.id},{self.created_at},{self.updated_at}"