from django.contrib import admin
from .models import CustomUser, Department, Achievement, Employee, AchievementEmployee

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_staff')
    search_fields = ('email', 'username')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'department')
    list_filter = ('department',)
    search_fields = ('name', 'email')
        # filter_horizontal removed for 'achievements' due to custom through model

@admin.register(AchievementEmployee)
class AchievementEmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee', 'achievement', 'achievement_date')
    list_filter = ('achievement_date',)