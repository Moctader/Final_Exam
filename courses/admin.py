from django.contrib import admin
from .models import Course

# # Register your models here.

# class CourseAdmin(admin.ModelAdmin):
#     list_display=['course_title','course_description','department']
    
# admin.site.register(Course, CourseAdmin)
admin.site.register(Course)







