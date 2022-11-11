from django.contrib import admin

from class_base_views.web.models import Employee


# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass

