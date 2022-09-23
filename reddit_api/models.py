from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)

class User(AbstractUser, BaseModel):
    bio = models.TextField(blank=True, null=True)
    reputation = models.IntegerField(default=0)