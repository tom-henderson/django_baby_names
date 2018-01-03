from django.db import models
from django.conf import settings


class Name(models.Model):
    name = models.CharField(max_length=80)


class NamePreferences(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    preference = models.ManyToManyField(Word, through='Preferences')


class Preferences(models.Model):
    name = models.ForeignKey(Name)
    user = models.ForeignKey(User)
    liked = models.BooleanField()
