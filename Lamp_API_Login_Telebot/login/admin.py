from django.contrib import admin
from .models import *

admin.site.register(Subscriber)

class Subscriberadmin (admin.ModelAdmin):
    class Meta:
        model = Subscriber
