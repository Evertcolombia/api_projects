from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import json

# local imports
from .serializers import BookSerializer, OwnerSerializer
from .models import Book, Owner


""" Public endpoints """
@api_view(['POST'])
@csrf_exempt
def register(request):
    """ Register a new user endpoint """
    serialized = OwnerSerializer(data=request.data)
    if serialized.is_valid():
        Owner.objects.create_user(
            serialized.data['username'],
            serialized.data['author'],
            serialized.data['password']
        )
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@csrf_exempt
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return JsonResponse({'books': serializer.data}, safe=False, status=status.HTTP_200_OK)
""""""


""" CRUD for book endpoints needs authentication"""
@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def my_books(request):
    user = request.user.id
    books = Book.objects.filter(added_by=user)
    serializer = BookSerializer(books, many=True)
    return JsonResponse({'books': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def upload_book(request):
    payload = json.loads(request.body)
    print(payload["book"])
    owner = Owner.objects.get(id=request.user.id)
    book = Book.objects.create(
        title = payload["book"]["title"],
        description = payload["book"]["description"],
        owner = owner,
        price = payload["book"]["price"],
    )
    serializer = BookSerializer(book)
    return JsonResponse({'books': serializer.data}, safe=False, status=status.HTTP_201_CREATED)

@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_book(request, book_id):
    user = request.user.id
    payload = json.loads(request.body)
    payload = payload["book"]
    print(payload)
    try:
        book_item = Book.objects.filter(owner=user, id=book_id)
        book_item.update(**payload)
        print(book_item)
        book = Book.objects.get(id=book_id)
        serializer = BookSerializer(book)
        return JsonResponse({'book': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
      return JsonResponse({'Error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
      return JsonResponse({'Error': "Muts review the payload"}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_book(request, book_id):
    user = request.user.id
    try:
        book = Book.objects.get(owner=user, id=book_id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)