from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Owner
# Register your models here.
class OwnerInline(admin.StackedInline):
    model = Owner
    can_delete = False
    verbose_name_plural = 'owner'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (OwnerInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)