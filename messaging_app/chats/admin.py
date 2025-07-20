from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Conversation, Message


# Customize the UserAdmin for your custom User model
# This is crucial for the admin to correctly handle your AbstractBaseUser
class CustomUserAdmin(BaseUserAdmin):
    # The fieldsets attribute defines the order, grouping, and display of fields in the admin form.
    # We must explicitly list all fields from AbstractBaseUser and PermissionsMixin,
    # and your custom fields.
    # Note: 'password', 'last_login', 'date_joined' are handled by AbstractBaseUser/PermissionsMixin
    # 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions' are from PermissionsMixin
    # 'date_joined' is not present in AbstractBaseUser, only in AbstractUser.
    # Since you define 'created_at', use that.

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', 'role')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'created_at')}), # Use created_at instead of date_joined
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active', 'role')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'role', 'groups')
    search_fields = ('email', 'first_name', 'last_name', 'phone_number')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',) # For many-to-many fields


# Register your custom User model with the custom admin class
admin.site.register(User, CustomUserAdmin)

# Register other models
admin.site.register(Conversation)
admin.site.register(Message)
