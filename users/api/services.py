from users.api.repositories import UserRepository
from django.core.exceptions import ObjectDoesNotExist

class UserService:

    @staticmethod
    def create_user(user_data):
        return UserRepository.create_user(user_data)
    
    @staticmethod
    def get_all_users():
        return UserRepository.get_all_users()
    
    @staticmethod
    def get_user(user_id):
        user = UserRepository.get_user_by_id(user_id)
        if not user:
            raise ObjectDoesNotExist("Usuario no encontrado")
        return user
    
    @staticmethod
    def update_user(user_id, user_data):
        user = UserService.get_user(user_id)
        return UserRepository.update_user(user, user_data)
    
    @staticmethod
    def delete_user(user_id):
        user = UserService.get_user(user_id)
        UserRepository.delete_user(user)