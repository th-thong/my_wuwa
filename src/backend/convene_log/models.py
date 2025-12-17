from django.db import models
import uuid
from game_account.models import GameAccount


class ConvenesLog(models.Model):
    
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    game_account = models.ForeignKey(GameAccount, on_delete=models.CASCADE)


    cardPoolType = models.CharField(max_length=255, verbose_name="Card Pool Type")
    resourceId = models.BigIntegerField(verbose_name="Resource ID")
    qualityLevel = models.IntegerField(verbose_name="Quality Level")
    resourceType = models.CharField(max_length=50, verbose_name="Resource Type")
    name = models.CharField(max_length=255, verbose_name="Name")
    count = models.IntegerField(verbose_name="Count")
    time = models.DateTimeField(verbose_name="Time")

    class Meta:
        verbose_name = "Convene Log"
        verbose_name_plural = "Convene Logs"
        ordering = ['-time']

    def __str__(self):
        return f"{self.name} - {self.time.strftime('%Y-%m-%d %H:%M:%S')} of {self.game_account.user.email} - {self.game_account.uid}"