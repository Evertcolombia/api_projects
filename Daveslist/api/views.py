from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

# local imports
from .serializers import BookSerializer
from .models import Book, User


# Create your views here.

@api_view(["GET"])
def welcome(request):
    content = { "message": "Welcome to Book store API" }
    return JsonResponse(content, status=200)


