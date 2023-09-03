from django.urls import path
from . import views

urlpatterns = [
    # path('create_course/', views.AddCourseForm.as_view(), name='create_course'),
    path('home/', views.search, name='SearchMovie'),
    path('create/', views.create_course, name='create_course'),
    # path('delete/<int:course_id>/', views.deleteCourse, name='delete_course'),
    # path('create/<int:course_id>/', views.deleteCourse, name='delete_course')

  

]