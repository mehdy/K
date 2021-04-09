from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from .apis import ProfileRegisterUpdateAPIView

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("", ProfileRegisterUpdateAPIView.as_view(), name="profile-register-update"),
]
