from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .views import RegisterView,LogoutView

urlpatterns = [
   path('api-jwt-auth/', TokenObtainPairView.as_view(),name='token_obtain_pair'),
   path('api-jwt-auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('api-jwt-auth/verify/', TokenVerifyView.as_view(), name='token_verify'),
   path('register/',RegisterView.as_view(),name='register'),
   path('logout/',LogoutView.as_view(),name='logout'),
]
