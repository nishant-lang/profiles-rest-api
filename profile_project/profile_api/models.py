from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

class UserProfileManager(BaseUserManager):
    """Manager for user profiile"""

    def create_user(self,email,name,password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have email address')
        email=self.normalize_email(email)
        user=self.model(email=email,name=name)

        user.set_password(password)        
        user.save(using=self._db)
        
        return user


    def create_superuser(self,email,name,password):
        """Create and save a new superuser with given details"""
        user=self.create_user(email,name,password)

        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """datbase model for user in the system"""
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    def get_full_name(self):
        """Retrive full name of the user"""
        return self.name
    def short_name(self):
        """Retrive short name"""
        return self.name

    def __str__(self):
        """Return string representations of our ouser"""
        return self.email


class ProfilefeedItem(models.Model):
    """Profile status update"""
    User_Profile=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE

    )
    status_text=models.CharField(max_length=255)
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """"Return the model as a string"""
        return self.status_text
        
