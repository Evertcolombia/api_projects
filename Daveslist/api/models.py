from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.conf import settings
from django.utils import timezone


from django.contrib.auth.models import  AbstractBaseUser, \
    BaseUserManager, PermissionsMixin


class OwnerManager(BaseUserManager):

    def create_user(self, username, author, password=None, **extra_fields):
        """ Creates and save new user """
        
        # normalize email
        user = self.model(**extra_fields)
        user.username = username
        user.author = author
        user.set_password(password)
        user.save(using=self._db)
        return user

    
class Owner(AbstractBaseUser, PermissionsMixin):
    """ custom user model that supports """
    # password field is inherit from AbstractBaseUser
    username = models.CharField(max_length=250, unique=True)
    author = models.CharField(max_length=250)
    created_at = models.DateTimeField(default=timezone.now)

    objects = OwnerManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['author']

    def __str__(self):
        """Return string representation of our user"""
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    """cover = models.ImageField(
        upload_to='bookstore/covers',
        default='bookstore/covers/empty_book.png',
        blank=True,
        null=True,
    )"""
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """Return string representation of a book"""
        return self.title