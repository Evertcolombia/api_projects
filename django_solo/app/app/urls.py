# django imports
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

#
from app import views as local_views
from posts import views as posts_views


urlpatterns = [
    # admin url
    path('admin/', admin.site.urls),
    # local urls
    path("hello/", local_views.hello_world),
    path("sort/", local_views.sorted_integers),
    path("valid/<str:name>/<int:age>/", local_views.validation),

    # posts module urls
    path('posts/', posts_views.list_posts),
    path('posts2/', posts_views.list_posts2),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
