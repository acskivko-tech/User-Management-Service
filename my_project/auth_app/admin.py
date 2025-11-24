from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from auth_app.models import UserModel, Status


# Register your models here.

@admin.register(UserModel)
class UserAPIAdmin(UserAdmin):
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'password',
        'city',
        'phone_number',
        'status'
    )
    list_display_links = ('username',)
    list_filter = ('status','first_name','last_name','city')


@admin.register(Status)
class StatusAPIAdmin(admin.ModelAdmin):
    list_display = ('status_name',)
    list_display_links = ('status_name',)
    list_filter = ('status_name',)
