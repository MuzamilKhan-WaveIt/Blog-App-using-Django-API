from django.contrib import admin
from .models import Model
# Register your models here.

class SiteModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'body', 'created_at', 'updated_at')

admin.site.register(Model, SiteModelAdmin)