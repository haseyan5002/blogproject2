from django.contrib import admin

# Register your models here.
from .models import NewsPost

admin.site.register(NewsPost)
