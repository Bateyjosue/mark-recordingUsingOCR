from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ModuleModel(models.Model):
    module_code             = models.CharField(primary_key = True, max_length = 10, blank = False, null = False, unique = True)
    module_title            = models.CharField(max_length = 200, blank = False, null = False)
    module_credit           = models.IntegerField()
    module_description      = models.TextField()
    add                     = models.DateTimeField(auto_now = True)
    update                  = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.module_title
class CourseModel(models.Model):
    user                    = models.ForeignKey(User, on_delete = models.CASCADE)
    module                  = models.ForeignKey(ModuleModel, on_delete = models.CASCADE)
    # module_title            = models.CharField(max_length = 200, blank = False, null = False)
    student_reg_number      = models.CharField(max_length = 50, blank = False, null = False)
    marks                   = models.IntegerField()
    state                   = (('Final', 'Final'), ('Provisory','Provisory'), ('Cancel','Cancel'))
    status                  = models.CharField(max_length =50, choices =state, default = 'Provisory')
    start_periode           = models.DateTimeField()
    end_periode             = models.DateTimeField()
    add                     = models.DateTimeField(auto_now = True)
    update                  = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        string =str(self.module)
        return string
    