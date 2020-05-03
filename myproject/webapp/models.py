from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save


class employees(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    emp_id = models.IntegerField()

    def __str__(self):
            return self.firstname

class JWTPayloadTrack(models.Model):
    username = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=200, null=True, blank=True)
    iat = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'JWT Payload Tracks'

    def __str__(self):
        return self.username
