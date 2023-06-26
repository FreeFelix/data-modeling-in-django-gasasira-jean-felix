from django.contrib import admin
from conferences.models import Conference, ScheduleManager

# Register your models here.
admin.site.register(Conference)
admin.site.register(ScheduleManager)
