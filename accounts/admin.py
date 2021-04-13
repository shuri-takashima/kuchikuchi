from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Connection

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields' : ('username', 'password')}),
        (('Personal_info'), {'fields' : (
            'first_name', 'last_name', 'email', 'avatar', 
            )}),
        (('Permissions'), {'fields' : ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (('Important dates'), {'fields' : ('last_login', 'date_joined')}),
    )
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Connection)