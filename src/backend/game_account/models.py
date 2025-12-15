from django.db import models
import uuid
from django.contrib.auth import get_user_model

User = get_user_model()


class GameAccount(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    oauth_code=models.CharField(max_length=40, verbose_name="OAuth Code",null=True)
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='game_accounts'
        )

    uid = models.CharField(max_length=10, verbose_name="UID")
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'uid'], name='unique_user_uid')
        ]
        verbose_name = "GameAcocunt"
        verbose_name_plural = "GameAccounts"
        
    
    def __str__(self):
        return f"Game account {self.uid} of {self.user.email}"