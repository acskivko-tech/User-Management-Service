from django.contrib.auth.models import AbstractUser
from django.db import models



# Create your models here.
class Status(models.Model):
    status_name = models.CharField()

    def __str__(self):
        return self.status_name

class UserModel(AbstractUser):
    city = models.CharField(blank=True,default='world',max_length=25)
    phone_number = models.CharField(blank=True,default='000-000-0000',max_length=20)
    status = models.ForeignKey(Status,on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.username
