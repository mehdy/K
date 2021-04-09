from rest_framework.permissions import BasePermission


class UnauthenticatedPost(BasePermission):
    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)

    def has_permission(self, request, view):
        return request.method == "POST"
