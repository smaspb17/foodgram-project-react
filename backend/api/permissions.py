from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminAuthorOrReadOnly(BasePermission):
    """
    Проверка является ли админом или автором
    """
    def has_permission(self, request, view):
        return (request.method in SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in SAFE_METHODS
                or request.user.is_superuser
                or obj.author == request.user)
