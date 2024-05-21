from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    application = models.CharField(max_length=255)