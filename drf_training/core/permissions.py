from rest_framework import permissions


class IsOwnerOrStaffOrReadOnly(permissions.BasePermission):
    message = "You do not have permission to update this book."

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner or request.user.is_staff
