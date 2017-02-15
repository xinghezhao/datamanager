from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Permission(models.Model):
    title = models.CharField(max_length=60)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class UserPermission(models.Model):
    user = models.ForeignKey(User)
    permission = models.ForeignKey(Permission)

    def __str__(self):
        return " - ".join([self.user.username, self.permission.title])

class Menu(models.Model):
    title = models.CharField(max_length=60)
    permission = models.ForeignKey(Permission, null=True)

    def __str__(self):
        return self.title
