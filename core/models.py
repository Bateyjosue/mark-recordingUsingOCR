from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CourseModel(models.Model):
    user                    = models.ForeignKey(User, on_delete = models.CASCADE)
    module_code             = models.CharField(max_length = 10, blank = False, null = False)
    module_title            = models.CharField(max_length = 200, blank = False, null = False)
    student_reg_number      = models.CharField(max_length = 50, blank = False, unique = True, null = False)
    marks                   = models.IntegerField(max_length = 5)
    start_periode           = models.DateTimeField()
    end_periode             = models.DateTimeField()
    add                     = models.DateTimeField(auto_now = True)
    update                  = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.module_code