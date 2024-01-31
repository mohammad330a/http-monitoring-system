from django.db import models


class Server(models.Model):
    address = models.CharField(max_length=255)
    success = models.IntegerField(default=0)
    failure = models.FloatField(default=0)
    last_failure = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
