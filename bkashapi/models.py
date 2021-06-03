from django.db import models

# Create your models here.
class BkashPayload(models.Model):
    payload = models.TextField()