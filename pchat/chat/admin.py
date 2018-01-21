from django.contrib import admin

# Register your models here.
from .models import Animal, Profile

admin.site.register(Animal)
admin.site.register(Profile)