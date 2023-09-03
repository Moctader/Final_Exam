from django import forms
from .models import Course
from django.forms import ModelForm

class CourseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['course_title'].widget.attrs.update({'class': 'form-control'})
        self.fields['department'].widget.attrs.update({'class': 'form-control'})
        self.fields['course_description'].widget.attrs.update({'class': 'form-control'})

    
    class Meta:
        model=Course
        fields=['course_title','department','course_description']
     
