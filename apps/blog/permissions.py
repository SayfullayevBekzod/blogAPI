from rest_framework.permissions import BasePermission
from rest_framework import permissions


class IsSuperUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_superuser:
            return True
        else:
            return False


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.user_id == request.user:
            return True
        else:
            return False


class IsStaffPermision(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_staff:
            return True
        else:
            return False
