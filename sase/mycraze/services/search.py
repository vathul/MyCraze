from django.contrib.auth.models import User
from django.db.models import Q

class UserSearchService:
    
    @staticmethod
    def get_users_by_name(q):
        user_list = None
        if q == None:
            user_list = User.objects.filter(Q(user_profile__isnull=False))
        else:
            user_list = User.objects.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q))
        return user_list
    
    @staticmethod
    def get_users_by_skills():
        print('skills')
        return ""
    
    @staticmethod
    def get_all_users(q):
        user_list = None
        if q == None:
            user_list = User.objects.filter(Q(user_profile__isnull=False))
        else:
            user_list = User.objects.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q))
        return user_list