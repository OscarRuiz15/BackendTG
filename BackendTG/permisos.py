import firebase_admin
from firebase_admin import credentials, auth
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

cred = credentials.Certificate("credenciales.json")
firebase_admin.initialize_app(cred)


class AuthFirebaseUser(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            return True
        except:
            raise PermissionDenied({"message": "You don't have permission to access"})


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            if request.method in permissions.SAFE_METHODS:
                return True
            return obj.lugar.propietario.uid == uid
        except:
            raise PermissionDenied({"message": "You don't have permission to access"})


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            print (uid)
            if request.method in permissions.SAFE_METHODS:
                return True
            return 'Dq2hAFrjjwTR0SeGrTpKm8jr9Eq1' == uid
        except:
            raise PermissionDenied({"message": "You don't have permission to access"})