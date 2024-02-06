from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password
from django.utils.crypto import get_random_string
from django.contrib.auth.models import AbstractUser
from django.db import models



class BaseUser(AbstractUser):
    # Base user model with common fields
    # class Meta:
    #     pass
    pass

class Installer(BaseUser):
    # Additional fields for installer users
    class Meta:
        proxy = True

class UserProfile(BaseUser):
    # Additional fields for user profile users
    class Meta:
        proxy = True



# class Installer(AbstractUser):
#     # Installer Profile model
#     pass
# class Installer(models.Model):
#     # Installer Profile model
#     username = models.CharField(max_length=100)
#     email = models.EmailField(default='janeDoe@greek.com')
#     password = models.CharField(max_length=100,default='password123')
    
#     first_name = models.CharField(max_length=30,default='Jane')
#     last_name = models.CharField(max_length=30,default='Doe')

    # REQUIRED_FIELDS = ['username']
    # USERNAME_FIELD = 'email'


# class UserProfile(models.Model):
#     # User Profile model
#     username = models.CharField(max_length=100)
#     email = models.EmailField(default='jamesBrown@greek.com')
#     password = models.CharField(max_length=100,default=make_password(password="password123"))

#     first_name = models.CharField(max_length=30,default='James')
#     last_name = models.CharField(max_length=30,default='Brown')

#     installer = models.ForeignKey(Installer, on_delete=models.SET_DEFAULT, default=None, null=True, related_name='users')


# # Creating an instance of installer_0
# installer_0, created = Installer.objects.get_or_create(username='installer_0')

# # Signal to handle deletion of installers
# @receiver(pre_delete, sender=Installer)
# def pre_delete_installer(sender, instance, **kwargs):
#     if instance != installer_0:
#         # Assign users within the deleted installer to installer_0
#         UserProfile.objects.filter(installer=instance).update(installer=installer_0)