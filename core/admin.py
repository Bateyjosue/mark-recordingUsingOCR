from django.contrib import admin
from .models import UpLoadImage, Marks, Student, Module, Enroll

# Register your models here.

@admin.register(UpLoadImage)
class UpLoadImageAdmin(admin.ModelAdmin):
    list_display = ('pk','user','picture', 'add')

@admin.register(Marks)
class MarksAdmin(admin.ModelAdmin):
    list_display = ('pk', 'student_reg_number', 'mark', 'update')
    list_filter = ('student_reg_number', 'update')

@admin.register(Student)
class StudemtAdmin(admin.ModelAdmin):
    list_display = ('pk','student_reg_number', 'name')

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('pk','name')

@admin.register(Enroll)
class EnrollAdmin(admin.ModelAdmin):
    list_display = ('pk','module_code', 'student_reg_number', 'due_period')