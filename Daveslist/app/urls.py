
from django.views.generic import TemplateView
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework.schemas import get_schema_view


urlpatterns = [
    path('api/', include('api.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('openapi/', get_schema_view(
        title="Card validation service",
        description="API developers hoping to use our service"
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]
