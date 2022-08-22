from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class IsSeller(permissions.BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'seller')