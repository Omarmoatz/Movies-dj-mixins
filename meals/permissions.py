from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        print(user.get_all_permissions())
        if user.is_staff:
            if user.has_perm("meals.view_meal"):
                return True
            if user.has_perm("meals.add_meal"):
                return True
            if user.has_perm("meals.change_meal"):
                return True
            if user.has_perm("meals.delete_meal"):
                return True
            return False
        return super().has_permission(request, view)