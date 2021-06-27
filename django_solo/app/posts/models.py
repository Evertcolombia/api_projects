from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """ Post table model """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Profile = models.OneToOneField('users.Profile', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    # photo = models.ImageField(upload_to='posts/photos')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ string representation"""
        return "{} by @{}".format(self.title, self.user.username)
