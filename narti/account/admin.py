from django.contrib import admin
from .models import *


class ComicsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_update', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    list_filter = ('time_create', 'is_published')
    list_editable = ('is_published', )
    search_fields = ('title', 'description')


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbr')
    list_display_links = ('name', 'abbr')
    search_fields = ('name',)


admin.site.register(Comics, ComicsAdmin)
admin.site.register(Language, LanguageAdmin)
