
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


@login_required
def index(request):
    # try:
    #     cam = VideoCamera()
    #     return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    # except :
    #     pass
    return render(request, 'dashboard.html')


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

class VideoCamera(object):
    # global video = None
    def __init__(self, request):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

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
                    "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY")
                    
                }

                response = requests.request("POST", url = url, headers = headers, data = payload, files = files)
                v = json.loads(response.text)
                val.append(v['value'])
                print(val)
                # reg = val[0].split('/')[0]
                # mark = val[0].split('/')[1]
                # print(f'Reg Number: {reg} & Mark: {mark}')
                # record_mark = Marks.objects.create(student_reg_number = reg, mark = mark)
                # record_mark.save()
                # val.clear()
            else:
                print("Error::Not Captured")

        elif key == ord('q'):
            cam.release()
            cv2.destroyAllWindows()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    context = {
        'mark' : Marks.objects.all(),
    }
    return render(request, 'capture.html', context)