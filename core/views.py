
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CourseModel as Course, ModuleModel

from edenai import OCR

import numpy as np
import cv2

import http.client
# Create your views here.
captured = ''
i = 0


@login_required
def index(request):
    courses = Course.objects.all().filter(user=not request.user)
    context = {
        'courses': Course.objects.all().filter(user=request.user)[:10],
        'count_course': Course.objects.all().distinct().count(),
        'dist_course': ModuleModel.objects.all()[:9],
        'get_status_Pro': Course.objects.all().filter(status='Provisory').count(),
        'get_status_Fin': Course.objects.all().filter(status='Final').count(),
        'get_status_Can': Course.objects.all().filter(status='Cancel').count(),
        'pro': (Course.objects.all().filter(status='Provisory').count()/Course.objects.all().distinct().count()) * 100,
        'fin': (Course.objects.all().filter(status='Final').count()/Course.objects.all().distinct().count()) * 100,
        'can': (Course.objects.all().filter(status='Cancel').count()/Course.objects.all().distinct().count()) * 100,
        'last_added': Course.objects.all().order_by('-add')[:5],
    }
    return render(request, 'dashboard.html', context)


@login_required
def record_mark(request):
    if request.method == 'GET':
        conn = http.client.HTTPSConnection(
            "cloudlabs-image-ocr.p.rapidapi.com")

        payload = "{% static 'images/3.jpg' %}"

        headers = {
            'content-type': "application/json",
            'X-RapidAPI-Host': "cloudlabs-image-ocr.p.rapidapi.com",
            'X-RapidAPI-Key': "d5e7bd069fmsh822a3ff6828266cp131b4ejsn99a6119f46b9"
        }

        conn.request("POST", "/ocr/recognizeUrl", payload, headers)

        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))

        print(data.decode("utf-8"))
        context = {
            'mark': data.decode("utf-8"),
        }
        return render(request, 'record.html', context)
    else:
        # image = request.POST['img']

        # img = cv2.imread('./static/images/3.jpg', 0)
        # cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        # cv2.imshow('image', img)
        # k = cv2.waitKey(0)
        # if k == 27:
        #     cv2.destroyAllWindows()
        # elif k == ord('s'):
        #     cap = cv2.imwrite('img.png', img)
        #     print(cap)
        #     cv2.destroyAllWindows()

        start_periode = request.POST['start']
        end_periode = request.POST['end']
    return render(request, 'record.html')


def capture(request):
    cam = cv2.VideoCapture(0)
    # cv2.namedWindow("Capture")
    counter = 0
    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to laoad...")
            break
        cv2.imshow("Capture", frame)
        k = cv2.waitKey(0)

        if k == ord('q'):
            print("Quitting...")
            break
        elif k == ord('s'):
            img = cv2.imwrite("capt_{}.png".format(counter), frame)
            counter +=1


    cam.release()
    cam.destroyAllWindows()
    context = {
        'img' : img,
    }
    return render(request, 'record.html', context)


# from edenai import OCR

# Get your API key here: https://app.edenai.run/admin/account
# ocr_apis = OCR("Your_API_key")

# result = ocr_apis.basic(
# # Available providers, languages and formats here: https://api.edenai.run/v1/redoc/#operation/OCR
#    providers=["google","amazon"],
#    language="en-US",
#    file="your_image.png")

# print(result)
