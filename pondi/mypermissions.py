from rest_framework import permissions
class MyAuth(permissions.IsAuthenticated):

    def has_permission(self, request, view):
        if request.method == 'OPTIONS':
            return True
        return super(MyAuth, self).has_permission(request, view)
