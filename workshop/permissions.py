from rest_framework import permissions
from .models import UserProfile


class AllowWorkshopHead(permissions.BasePermission):
    message = "You are not authorized to perform this task"

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        # pylint: disable=no-member
        profile = UserProfile.objects.get(user=request.user)
        # pylint: disable=no-member
        if obj.club is not None:
            club = obj.club
            if club in profile.get_club_privileges():
                return True
        elif obj.entity is not None:
            entity = obj.entity
            if entity in profile.get_entity_privileges():
                return True
        return False


class AllowWorkshopHeadOrContact(permissions.BasePermission):
    message = "You are not authorized to perform this task"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            return False
        # pylint: disable=no-member
        profile = UserProfile.objects.get(user=request.user)
        # pylint: disable=no-member
        if obj.club is not None:
            club = obj.club
            if (club in profile.get_club_privileges()
                    or obj in profile.organized_workshops.all()):
                return True
        elif obj.entity is not None:
            entity = obj.entity
            if (entity in profile.get_entity_privileges()
                    or obj in profile.organized_workshops.all()):
                return True
        return False


class AllowAnyClubHead(permissions.BasePermission):
    message = "You are not authorized to perform this task"

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        # pylint: disable=no-member
        profile = UserProfile.objects.get(user=request.user)
        if profile.get_club_privileges():
            return True
        return False


class AllowAnyClubOrEntityHead(permissions.BasePermission):
    message = "You are not authorized to perform this task"

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        # pylint: disable=no-member
        profile = UserProfile.objects.get(user=request.user)
        if profile.get_club_privileges() or profile.get_entity_privileges():
            return True
        return False


class AllowAnyClubHeadOrContact(permissions.BasePermission):
    message = "You are not authorized to perform this task"

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        # pylint: disable=no-member
        profile = UserProfile.objects.get(user=request.user)
        if profile.get_club_privileges() or profile.get_workshop_privileges():
            return True
        return False


class AllowAnyEntityHeadOrContact(permissions.BasePermission):
    message = "You are not authorized to perform this task"

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        # pylint: disable=no-member
        profile = UserProfile.objects.get(user=request.user)
        if profile.get_entity_privileges() or profile.get_workshop_privileges():
            return True
        return False


class AllowWorkshopHeadOrContactForResource(permissions.BasePermission):
    message = "You are not authorized to perform this task"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            return False
        # pylint: disable=no-member
        profile = UserProfile.objects.get(user=request.user)
        # pylint: disable=no-member
        if obj.workshop.club is not None:
            club = obj.workshop.club
            if (club in profile.get_club_privileges()
                    or obj.workshop in profile.organized_workshops.all()):
                return True
        elif obj.workshop.entity is not None:
            entity = obj.workshop.entity
            if (entity in profile.get_entity_privileges()
                    or obj.workshop in profile.organized_workshops.all()):
                return True
        return False


class AllowParticularClubHead(permissions.BasePermission):
    message = "You are not authorized to perform this task"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            return False
        # pylint: disable=no-member
        profile = UserProfile.objects.get(user=request.user)
        club = obj
        if club in profile.get_club_privileges():
            return True
        return False


class AllowParticularCouncilHead(permissions.BasePermission):
    message = "You are not authorized to perform this task"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            return False
        # pylint: disable=no-member
        profile = UserProfile.objects.get(user=request.user)
        council = obj
        if council in profile.get_council_privileges():
            return True
        return False


class AllowParticularEntityHead(permissions.BasePermission):
    message = "You are not authorized to perform this task"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            return False
        # pylint: disable=no-member
        profile = UserProfile.objects.get(user=request.user)
        entity = obj
        if entity in profile.get_entity_privileges():
            return True
        return False


class AllowAnyEntityHead(permissions.BasePermission):
    message = "You are not authorized to perform this task"

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        # pylint: disable=no-member
        profile = UserProfile.objects.get(user=request.user)
        if profile.get_entity_privileges():
            return True
        return False
