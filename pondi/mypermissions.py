from rest_framework import permissions
class MyAuth(permissions.IsAuthenticated):

    def has_permission(self, request, view):
        if request.method == 'OPTIONS':
            return True
        return request.user and request.user.is_authenticated
