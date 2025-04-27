from django.contrib import admin

from .models import UserDetails


@admin.register(UserDetails)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["Username", "Email", "Password"]
