from django.db import models
from django.contrib.auth.models import AbstractBaseUser
#let create diffrent permisision users
from django.contrib.auth.models import PermissionsMixin 
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


"""functions within the manager are use to manipulate objects 
    whithin the models than manager is for"""


class UserProfileManager(BaseUserManager):
    """Manage class for user profiles"""
    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        # it line says it can use multiple db
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save nuew super user with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Data model for the users profile in the system """
    email = models.EmailField(max_length=150, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # call custom model mannager for the user
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""

    def get_short_name(self):
        """Retrieve short name of user"""

    def __str__(self):
        """Return string representation of our user"""
        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL, # from where will be assosiated
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text


