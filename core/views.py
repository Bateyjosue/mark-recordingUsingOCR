
import threading
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UpLoadImage, Marks
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

from .forms import ImageForm
import cv2
import requests
from urllib.parse import urlparse
import json
import math
import os

from .models import Student, Module, Enroll, Capture


@login_required
def index(request):
    all_marks = Capture.objects.all()[:5]
    recent_marks = Capture.objects.all().order_by('due_period')[:5]
    all_student = Capture.objects.all().distinct()

    all_student_grade= Capture.objects.all().count()
    student_with_A = Capture.objects.filter(marks__gte = 80).count()
    A = (student_with_A/all_student_grade) * 100 
    student_with_FAIL = Capture.objects.filter(marks__lte = 49).count()
    FAIL = (student_with_FAIL/all_student_grade) * 100 
    student_with_B = Capture.objects.filter(marks__gte = 70).count() & Capture.objects.filter(marks__lte = 79 ).count()
    B = (student_with_B/all_student_grade) * 100 
    student_with_C = Capture.objects.filter(marks__gte = 60).count() & Capture.objects.filter(marks__lte = 69 ).count()
    C = (student_with_C/all_student_grade) * 100 
    student_with_D = Capture.objects.filter(marks__gte = 50).count() & Capture.objects.filter(marks__lte = 59 ).count()
    D= (student_with_D/all_student_grade) * 100 

    total_student = Capture.objects.all().distinct().count()
    high_mark = Capture.objects.all().order_by('student_reg_number','marks')[2]
    low_mark = Capture.objects.all().order_by('marks')[0]
    context = {
        'all_marks': all_marks,
        'recent_marks': recent_marks,
        'all_student': all_student,
        'all_student_grade' : all_student_grade,
        'student_with_A' : student_with_A,
        'student_with_B' : student_with_B,
        'student_with_C' : student_with_C,
        'student_with_D' : student_with_D,
        'student_with_FAIL' : student_with_FAIL,
        'A' : A,
        'FAIL' : FAIL,
        'B' : B,
        'C' : C,
        'D' : D,
        'total_student' : total_student,
        'high_mark' : high_mark,
        'low_mark' : low_mark,
        


    }
    return render(request, 'dashboard.html', context)


@login_required
def record_mark(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        for img in image:
            upload = UpLoadImage.objects.create(user = request.user, picture = img)
            upload.save()
        print(upload)
        # message  = messages.success(request, "saved")
        context ={
            # 'message': message,
        }
        return render(request, 'record.html', context)
    elif request.method == 'GET':
        images = UpLoadImage.objects.all()
        context ={
            'images': images,
        }
        return render(request, 'record.html', context)

@gzip.gzip_page
def capture(request):
    val = []
    v = ''
    cam = cv2.VideoCapture(0)
    files = '/home/josh-ishara/Documents/Project/Memoir/mark-recordingUsingOCR/img.png'
    while True:
        ret, frame = cam.read()
        if not ret: 
            print ("Error reading")
            break
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)

        if key == ord('s'):
            img_write = cv2.imwrite('img.png', frame)
            if img_write:
                pa = cv2.imread('/home/josh-ishara/Documents/Project/Memoir/mark-recordingUsingOCR/img.png')
                print(files)
                cv2.imshow('Show Image Camptured',pa)
                url = 'https://pen-to-print-handwriting-ocr.p.rapidapi.com/recognize/'
                image = urlparse('/home/josh-ishara/Documents/Project/Memoir/mark-recordingUsingOCR/img.png')
                image = image.path
                image = image.split('/')
                image = image[-1]
                payload = {}
                files = [
                    ('srcImg', (image, open('/home/josh-ishara/Documents/Project/Memoir/mark-recordingUsingOCR/img.png', 'rb'), 'image/png'))
                ]
                headers = {
                    "X-RapidAPI-Key": "b55584df9dmshd8095426dd08d09p1276dejsn105ade750933"
                    
                }
                # try:

                response = requests.request("POST", url = url, headers = headers, data = payload, files = files)
                v = json.loads(response.text)
                val.append(v['value'])
                print(v)
                booklet = val[0].split('\n')[0]
                code = val[0].split('\n')[1]
                due = val[0].split('\n')[2]
                reg = val[0].split('\n')[3].split('/')[0]
                mark = val[0].split('\n')[3].split('/')[1]
                # mark = val[0].split('/')[0]
                # mark = val[0].split('/')[1]
                print(f'Reg Number: {reg} & Mark: {mark} Booklet: {booklet} Module: {code} Period : {due}')
                # record_mark = Marks.objects.create(student_reg_number = reg, mark = mark)
                # record_mark.save()
                if Student.objects.filter(student_reg_number = reg).exists():
                    if Enroll.objects.filter(student_reg_number = reg).exists():
                        messages.error(request, 'This Reg Number is already in Captured')
                    else:
                        save_captured = Capture.objects.create(module_code = code, student_reg_number = reg, due_period = due, marks = mark, booklet = booklet)
                        save_captured.save()

                else:
                    messages.error(request, 'Student Not Found, Check well the regnumber')

                val.clear()
                # except:
                #     return render(request, 'error.html', {'message': messages})
            else:
                print("Error::Not Captured")

        elif key == ord('q'):
            cam.release()
            cv2.destroyAllWindows()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    context = {
        'mark' : Capture.objects.all(),
    }
    return render(request, 'capture.html', context)