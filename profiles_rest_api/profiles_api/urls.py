from django.urls import path, include
from profiles_api import views
from rest_framework.routers import  DefaultRouter


router = DefaultRouter()

"""use base_name on register when youre creating a viewset
that doesn't have a query_set from the view that corresponds
or if you want overwrite the query_set name"""
router.register('hello-viewset', views.HelloViewSet, base_name="hello=viewset")
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)



urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]