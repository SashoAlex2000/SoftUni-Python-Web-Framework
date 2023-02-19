from django.contrib import admin

from sample_rest_api.api_todos.models import Todo, Category


# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

