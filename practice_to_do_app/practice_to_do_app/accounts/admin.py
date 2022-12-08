from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

# Register your models here.

UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(auth_admin.UserAdmin):
    pass
