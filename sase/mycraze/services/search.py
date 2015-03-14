from django.contrib.auth.models import User
from django.db.models import Q

class UserSearchService:

    @staticmethod
    def get_users_by_name(query):
        user_list = None
        if query == None:
            user_list = User.objects.filter(Q(user_profile__isnull=False))
        else:
            user_list = User.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query)).distinct()
        return user_list
    
    @staticmethod
    def get_users_by_skills(query):
        user_list = None
        if query == None:
            user_list = User.objects.filter(Q(user_profile__isnull=False))
        else:            
            user_list = User.objects.filter(Q(user_profile__skill_section__skill_items__skill__icontains=query)).distinct()
        return user_list
    
    @staticmethod
    def get_all_users(query):
        user_list = None
        if query == None:
            user_list = User.objects.filter(Q(user_profile__isnull=False))
        else:
            user_list = User.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(user_profile__skill_section__skill_items__skill__icontains=query)).distinct()
        return user_list