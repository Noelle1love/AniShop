from django.contrib import admin

# Register your models here.
from main.models import Main, AboutUs, Team, Blog, ContactSupport


@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ('site_name',)

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ("photo", "description", "year_in_buisness", "happy_people", "sales", "award_winning")

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('photo', 'name', 'job_title', 'instagram', 'facebook')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'description')

@admin.register(ContactSupport)
class ContactSupportAdmin(admin.ModelAdmin):
    list_display = ('coordinates', 'hot_line', 'email_support', 'email_info')
