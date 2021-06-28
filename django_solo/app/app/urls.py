# django imports
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

# apps views
from app import views as local_views
from posts import views as posts_views
from users import views as users_views

urlpatterns = [
    # admin url
    path('admin/', admin.site.urls),
    
    # local urls
    path("hello/", local_views.hello_world, name="hello"),
    path("sort/", local_views.sorted_integers, name="sorted"),
    path("valid/<str:name>/<int:age>/", local_views.validation, name="validation"),

    # posts module urls
    path('posts/', posts_views.list_posts, name="feed"),
    
    # users urls
    path('users/login/', users_views.login_view, name="login"),
    path('users/logout', users_views.logout_view, name='logout')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
