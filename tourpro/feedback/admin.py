from django.contrib import admin
from .models import Feedback
from .models import Event

admin.site.register(Event)
admin.site.register(Feedback)
