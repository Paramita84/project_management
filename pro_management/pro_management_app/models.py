from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    # add additional fields in here
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'
    username = models.CharField(max_length=30,unique=True)
    department = models.CharField(max_length=30)
    date_of_join = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.email
