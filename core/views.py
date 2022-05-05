
import threading
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UpLoadImage
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

from .forms import ImageForm



@login_required
def index(request):
    return render(request, 'dashboard.html')


@login_required
def record_mark(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        for img in image:
            upload = UpLoadImage.objects.create(user = request.user, picture = img)
            upload.save()
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

# class Video(object):
#     def __init__(self, request):
#         self.video = cv2.VideoCapture(0)
#         (self.grabbed, self.frame) = self.video.read()
#         threading.Thread(target=self.update, args=()).start()

#     def __del__(self):
#         self.video.release()

#     def get_frame(self):
#         image = self.frame
#         _, jpeg = cv2.imencode('.jpg', image)
#         return jpeg.tobytes()

#     def update(self):
#         while True:
#             (self.grabbed, self.frame) = self.video.read()

# def gen(self):
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# def capture(request):
#     pass
