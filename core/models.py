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
    user        = models.ForeignKey(User, on_delete = models.CASCADE, default= 1)
    student_reg_number  = models.CharField(max_length=50)
    mark                = models.IntegerField()
    add                 = models.DateTimeField(auto_now = True)
    update              = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.student_reg_number