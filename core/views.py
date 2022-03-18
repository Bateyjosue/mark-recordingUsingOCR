from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CourseModel as Course, ModuleModel

# Create your views here.

@login_required
def index(request):
    courses = Course.objects.all().filter(user = not request.user)
    context = {
        'courses'           : Course.objects.all().filter(user = request.user)[:10],
        'count_course'      : Course.objects.all().distinct().count(),
        'dist_course'       : ModuleModel.objects.all()[:9],
        'get_status_Pro'    : Course.objects.all().filter(status = 'Provisory').count(),
        'get_status_Fin'    : Course.objects.all().filter(status = 'Final').count(),
        'get_status_Can'    : Course.objects.all().filter(status = 'Cancel').count(),
        'pro'               : (Course.objects.all().filter(status = 'Provisory').count()/Course.objects.all().distinct().count()) * 100,
        'fin'               : (Course.objects.all().filter(status = 'Final').count()/Course.objects.all().distinct().count()) * 100,
        'can'               : (Course.objects.all().filter(status = 'Cancel').count()/Course.objects.all().distinct().count()) * 100,
        'last_added'        : Course.objects.all().order_by('-add')[:5],
    }
    return render(request, 'dashboard.html', context)

@login_required
def record_mark(request):
    return render(request, 'record.html')