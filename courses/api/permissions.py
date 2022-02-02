from rest_framework.permissions import BasePermission


class IsEnrolled(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Only enrolled students can access course's contents.
        return obj.students.filter(id=request.user.id).exists()
