from django.contrib import admin

from .models import Badge


class BadgeAdmin(admin.ModelAdmin):
    fields = ('icon',)
    list_display = ('id', 'level')

admin.site.register(Badge, BadgeAdmin)
