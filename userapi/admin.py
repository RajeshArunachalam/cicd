from django.contrib import admin
from .models import *
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "is_staff", "id")
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ["user_permissions", "groups"]
    inlines = [UserProfileInline]
    extra = 1


admin.site.register(UserProfile)