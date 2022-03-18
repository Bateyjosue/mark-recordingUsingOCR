from django.contrib import admin
from .models import CourseModel, ModuleModel

# Register your models here.

@admin.register(CourseModel)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ('user','module','status', 'student_reg_number', 'marks', 'start_periode', 'end_periode')
    fields = []
    
@admin.register(ModuleModel)
class ModuleModelAdmin(admin.ModelAdmin):
    list_display = ('module_code', 'module_title', 'module_description', 'module_credit')