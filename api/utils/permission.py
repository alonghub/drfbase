from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):
    message = "必须是xxx才可以访问"

    def has_permission(self, request, view):
        # if request.user.user_type == 3:
        #     return False
        return True
