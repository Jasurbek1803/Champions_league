from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser


class MyUserAdmin(UserAdmin):
    list_display = ("username", "email", "is_staff")
    search_fields = ("username", "email")
    list_filter = ("username", "is_staff")  # Add fields for filtering
    filter_horizontal = ()


admin.site.register(MyUser, MyUserAdmin)
