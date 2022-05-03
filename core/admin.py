from django.contrib import admin
from .models import UpLoadImage

# Register your models here.

@admin.register(UpLoadImage)
class UpLoadImageAdmin(admin.ModelAdmin):
    list_display = ('pk','user','picture', 'add')