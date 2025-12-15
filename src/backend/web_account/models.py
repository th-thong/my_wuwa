from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import uuid

class WebAccount(AbstractBaseUser):
    
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    password = models.CharField(max_length=255, verbose_name="Password")
    email = models.EmailField(verbose_name="Email")

    class Meta:
        verbose_name = "WebAccount"
        verbose_name_plural = "WebAccounts"

    def __str__(self):
        return self.email
