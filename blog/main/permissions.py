from rest_framework.permissions import BasePermission

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsAuthor(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_object_permission(self, request, view, obj):
        print('HEYYYYYYYYYYYYYYYYYYYYYYY')
        print(request.user, obj.author)
        ans = bool(
            request.method in SAFE_METHODS or
            request.user.is_authenticated and
            request.user == obj.author
        )
        print(ans)
        return ans

