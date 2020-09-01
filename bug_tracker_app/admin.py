from django.contrib import admin
from bug_tracker_app.models import MyUser, Ticket
from django.contrib.auth.admin import UserAdmin


admin.site.register(MyUser, UserAdmin)
admin.site.register(Ticket)
