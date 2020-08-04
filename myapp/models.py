from django.db import models
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
# from django.core.validators import RegexValidator
# Create your models here.

# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)

class Address(models.Model):

    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    pincode = models.PositiveIntegerField()
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.street_address

class Profile(models.Model):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'

    Choices = (
    (Male,'Male'),
    (Female,'Female'),
    (Other, 'Other')
    )

    user = models.OneToOneField(User,related_name='user', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13, unique=True)
    gender = models.CharField(max_length=10, choices = Choices, default=Male, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    date_of_birth = models.DateTimeField(blank=True)
    permanent_address = models.OneToOneField(Address,related_name='permanent_address',on_delete=models.CASCADE)
    company_address = models.OneToOneField(Address, related_name='company_address', on_delete=models.CASCADE)
    friends = models.ManyToManyField("self",related_name='friends', blank=True)



    def __str__(self):
        return self.user.username
