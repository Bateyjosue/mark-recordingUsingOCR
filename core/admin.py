from django.contrib import admin
from .models import UpLoadImage, Marks

# Register your models here.

@admin.register(UpLoadImage)
class UpLoadImageAdmin(admin.ModelAdmin):
    list_display = ('pk','user','picture', 'add')

@admin.register(Marks)
class MarksAdmin(admin.ModelAdmin):
    list_display = ('pk', 'student_reg_number', 'mark')