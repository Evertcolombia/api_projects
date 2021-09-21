from django.urls import path
from . import views

urlpatterns = [
    # public endpoints
    path('books', views.get_books),
    path('register', views.register),

    # crud for auth users
    path('my_books', views.get_books),
    path('upload', views.upload_book),
    path('update/<int:book_id>', views.update_book),
    path('delete/<int:book_id>', views.delete_book),
]