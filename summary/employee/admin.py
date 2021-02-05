from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Employee, Department
from simple_history.admin import SimpleHistoryAdmin


class EmployeeAdmin(SimpleHistoryAdmin):
    list_display = ['first_name', 'last_name', 'department']
    list_filter = ['department']



class DepartmentAdmin(SimpleHistoryAdmin):
    pass


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)
