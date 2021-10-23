from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "Buraya erişmek için gereken yetkiye sahip değilsiniz"

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
