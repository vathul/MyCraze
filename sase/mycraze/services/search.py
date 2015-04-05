"""This module contains classes pertaining to the forms used by the user to
add and edit various items in the user resume page"""

__author__ = "Srikrishnan Suresh"
__copyright__ = "Copyright 2015, MyCraze"
__version__ = "1.0.1"

from django.contrib.auth.models import User
from django.db.models import Q


class UserSearchService:
    """This module contains service classes for performing services related
searching user profiles."""

    @staticmethod
    def get_users_by_name(query):
        """This static method searches for all users with given query in their
        first name or last name or query as one of their skills."""

        user_list = None
        if query == None:
            user_list = User.objects.filter(Q(user_profile__isnull=False))
        else:
            user_list = User.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query)).distinct()
        return user_list
    
    @staticmethod
    def get_users_by_skills(query):
        """This static method searches for all users with given query
        as one of their skills."""

        user_list = None
        if query == None:
            user_list = User.objects.filter(Q(user_profile__isnull=False))
        else:            
            user_list = User.objects.filter(Q(user_profile__skill_section__skill_items__skill__icontains=query)).distinct()
        return user_list
    
    @staticmethod
    def get_all_users(query):
        """This static method searches for all users with given query in their
        first name or last name."""

        user_list = None
        if query == None:
            user_list = User.objects.filter(Q(user_profile__isnull=False))
        else:
            user_list = User.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(user_profile__skill_section__skill_items__skill__icontains=query)).distinct()
        return user_list