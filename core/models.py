from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UpLoadImage(models.Model):
    user        = models.ForeignKey(User, on_delete = models.CASCADE)
    picture     = models.ImageField(upload_to='images')
    add         = models.DateTimeField(auto_now = True)
    update      = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.picture.name)

class Marks(models.Model):
    user                = models.ForeignKey(User, on_delete = models.CASCADE, default= 1)
    student_reg_number  = models.CharField(max_length = 50)
    mark                = models.IntegerField()
    add                 = models.DateTimeField(auto_now = True)
    update              = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.student_reg_number

class Student(models.Model):
    student_reg_number  = models.CharField(primary_key = True,max_length = 20)
    name                = models.CharField(max_length = 100)
    mail                = models.EmailField(max_length = 100)
    phone               = models.CharField(max_length = 20)
    photo               = models.ImageField(upload_to = 'student/')
    address             = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.student_reg_number

class Module(models.Model):
    code                = models.CharField(primary_key = True, max_length = 10)
    name                = models.CharField(max_length = 100)
    description         = models.TextField()
    department          = models.CharField(max_length = 100)
    lecturer            = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.code

class Enroll(models.Model):
    module_code         = models.ForeignKey(Module, on_delete = models.CASCADE)
    student_reg_number  = models.ForeignKey(Student, on_delete = models.CASCADE)
    due_period          = models.DateTimeField()
    marks               = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.student_reg_number