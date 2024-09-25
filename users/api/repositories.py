from users.models import User

class UserRepository:

    @staticmethod
    def get_all_users():
        return User.objects.all()
    
    @staticmethod
    def get_user_by_id(user_id):
        return User.objects.filter(id=user_id).first()
    
    @staticmethod
    def create_user(user_data):
        password = user_data.pop('password')
        user = User(**user_data)
        user.set_password(password)
        user.save()
        return user
    
    @staticmethod
    def update_user(user, user_data):
        password = user_data.pop('new_password', None)
        for key, value in user_data.item():
            setattr(user, key, value)
        if password:
            user.set_password(password)
        user.save()
        return user
    
    @staticmethod
    def delete_user(user):
        user.delete()
