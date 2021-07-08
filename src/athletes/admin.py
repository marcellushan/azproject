from django.contrib import admin

from athletes.models import Athlete, Family, School, Year

# Register your models here.
admin.site.register(Athlete)
admin.site.register(Family)
admin.site.register(School)
admin.site.register(Year)
