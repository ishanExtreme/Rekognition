from django.db import models
from django.utils import timezone
import uuid
# Create your models here.


class InputVideo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=80)
    isProcessed = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.id


class InputImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=80)
    isProcessed = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.id


class InputEmbed(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    title = models.CharField(max_length=80)
    fileurl = models.CharField(max_length=100, editable=False)
    created_on = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.id