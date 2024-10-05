from rest_framework import permissions


class IsOwnerOrStaffOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow all GET requests
        if request.method == "GET":
            return True

        # Require authentication for all other methods
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow GET requests for any user
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the user is the owner or an admin for PUT and DELETE
        return request.user == obj.owner or request.user.is_staff
