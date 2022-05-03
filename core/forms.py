from django import forms
from .models import UpLoadImage

class ImageForm(forms.ModelForm):
    class Meta:
        model = UpLoadImage
        fields = ('picture',)