from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Profile(models.Model):
    OWNER = "OW"
    VET = "VT"
    USER_TYPE_CHOICES = (
        (OWNER, 'Owner'),
        (VET, "Vet"))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(
        max_length=2,
        choices=USER_TYPE_CHOICES,
        default=OWNER,
    )

    def __str__(self):
        return str(self.user)
