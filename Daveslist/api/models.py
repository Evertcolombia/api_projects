from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.conf import settings
from django.utils import timezone


from django.contrib.auth.models import  AbstractBaseUser, \
    BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """ Creates and save new user """
        if not email:
            raise ValueError("Users must have and email address")
        
        # normalize email
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ custom user model that supports """

    # password field is inherit from AbstractBaseUser
    email = models.EmailField(max_length=255, unique=True)
    author = models.CharField(max_length=150, unique=True)
    created_date = models.DateTimeField(default=timezone.now)

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['author']

    def __str__(self):
        """Return string representation of our user"""
        return self.email


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # cover
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_date = models.DateTimeField(default=timezone.now)