from django.contrib import admin
from mapbox_location_field.admin import MapAdmin

from .models import Map
# Register your models here.
admin.site.register(Map, MapAdmin)