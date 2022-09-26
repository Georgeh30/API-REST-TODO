from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.

        # Condicion para poder ver el detalle de cada objeto aunque no sea el usuario quien lo creo
        if request.method in permissions.SAFE_METHODS:
            return True

        # Condicion para poder modificar y eliminar el objeto solo el usuario quien lo creo
        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user