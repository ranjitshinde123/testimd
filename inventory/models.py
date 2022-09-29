
from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser
# from .manager import UserManager

# class User(AbstractUser):
#     phone_number=models.CharField(max_length=12,unique=True)
#     is_phone_verified=models.BooleanField(default=False)
#     otp=models.CharField(max_length=6,null=True)
#
#     USERNAME_FIELD = 'phone_number'
#     REQUIRED_FIELDS = []
#     objects = UserManager()


# stock
class Stock(models.Model):
    # status_choices = [
    #              ('CON', 'CONSUMABLE'),
    #              ('NON', 'NON-CONSUMABLE'),
    #          ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    category=models.CharField(max_length=30)
    subcategory=models.CharField(max_length=30)
    # type=models.CharField(max_length=50,choices=status_choices)
    type=models.CharField(max_length=20)
    size=models.CharField(max_length=50)
    label_code=models.CharField(max_length=20,default="")
    quantity = models.IntegerField(default=1)
    description=models.TextField()
    # user=models.OneToOneField(User,on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)



def __str__(self):
        return self.name



