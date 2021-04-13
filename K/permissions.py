from django.contrib.auth import get_user_model
from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class UnauthenticatedPost(BasePermission):
    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)

    def has_permission(self, request, view):
        return request.method == "POST"


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, get_user_model()):
            return request.user.pk == obj.pk
        return request.user.pk == obj.owner.pk
