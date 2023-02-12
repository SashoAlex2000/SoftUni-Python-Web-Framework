from django.contrib import admin

from rest_api_lecture.web_api.models import Employee, Department


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    def __str__(self):
        return f'Bazniga'
