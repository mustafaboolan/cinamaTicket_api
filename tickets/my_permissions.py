from rest_framework import permissions

# this function from doc django with our edits
class Just_For_Creator(permissions.BasePermission):
    def has_obj_perms(self, request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
