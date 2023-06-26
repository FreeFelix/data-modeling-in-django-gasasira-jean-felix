from django.contrib import admin
from speakers.models import Session, Attendee, Speaker


# Register your models here.
admin.site.register(Attendee)
admin.site.register(Session)
admin.site.register(Speaker)
