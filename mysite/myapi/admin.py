
from django.contrib import admin

# Register your models here.

from .models import Hero, Villian

admin.site.register(Hero)
admin.site.register(Villian)
