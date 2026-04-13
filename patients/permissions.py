from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):

        # Block if not logged in
        if not request.user or not request.user.is_authenticated:
            return False

        # Allow read-only for any logged in user
        if request.method in SAFE_METHODS:
            return True

        # Only staff can modify
        return request.user.is_staff