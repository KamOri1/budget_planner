from django.contrib import admin

from .models import Notification

admin.site.register(Notification)

# class NotificationAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'type', 'name')
