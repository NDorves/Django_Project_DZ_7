from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


# class IsOwnerOrReadOnly(BasePermission):   #Разреш-т редакт-ние объект. только их владельцам, остальным - только чтение
#     def has_object_permission(self, request, view, obj):     # Все пользователи могут просматривать
#         if request.method in ['GET', 'HEAD', 'OPTIONS']:
#             return True
#         return obj.owner == request.user    # Только владелец может изменять объект
#
#
# class IsAdminOrOwner(BasePermission):
#     def has_object_permission(self, request, view, obj): # Все пользователи могут просматривать
#         if request.method in ['GET', 'HEAD', 'OPTIONS']:
#             return True
#         # Только администратор или владелец может изменять объект
#         return request.user.is_staff or obj.owner == request.user
#