from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from practice_to_do_app.to_do_app.models import Task

# Register your models here.

UserModel = get_user_model()


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'urgency_level')

