from rest_framework import serializers
from api.models import Owner, Book

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['id', 'username', 'author', 'password']
        

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'owner',\
                    'price', 'created_at']