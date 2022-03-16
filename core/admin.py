from django.contrib import admin
from .models import CourseModel

# Register your models here.

@admin.register(CourseModel)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ('user','module_code', 'module_title', 'student_reg_number', 'marks', 'start_periode', 'end_periode')
    fields = []