from django.contrib import admin

from examproject.exam.models import Profile, Item


# Register your models here.
@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass