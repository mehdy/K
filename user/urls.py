from django.urls import path

from .apis import ProfileRegisterUpdateAPIView

urlpatterns = [
    path("", ProfileRegisterUpdateAPIView.as_view(), name="profile-register-update"),
]
