from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
# from .forms import CourseForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Course
from django.db import IntegrityError
from django.db.models import Q
from .forms import CourseForm



# Create your views here.

# def create_course(request):
#     if request.method == 'POST':
#         form = CourseForm(request.POST)
#         print(form)
#         if form.is_valid():
#             try:
#                 instance = form.save(commit=False) 
#                 instance.user=request.user
#                 instance.save()
#             except IntegrityError:
#                 print('Error occured')
                
          
#             return redirect('create_course')
#     else:
#         form = CourseForm()
#     return render(request, 'CourseCreation.html', {'form': form})

# class AddCourseForm(CreateView):
#     model=Course
#     template_name='CourseCreation.html'
#     form_class=CourseForm
#     success_url=reverse_lazy('course_list')


def search (request):
    searchTerm=request.GET.get('SearchMovie')
    if searchTerm:
        courses=Course.objects.filter(Q(course_title__icontains=searchTerm)|Q(department__icontains=searchTerm))

    else:
        courses="Search Not Found"
    #     courses=Course.objects.all()
    # all_course=courses=Course.objects.all()
    return render(request, 'search.html', {'searchTerm':searchTerm, 'courses':courses})


# def create_course(request):
#     if request.method=='GET':
#         return render(request, 'create_course.html', { 'form':CourseForm()})
#     else: 
#         try:
#             form=CourseForm(request.POST)
#             instance=form.save(commit=False)
#             instance.user=request.user
#             instance.save()
#             return redirect('SearchMovie')
#         except ValueError:
#             return render (request,'create_course.html', {'form':CourseForm(), 'error':'Bad data Given'} )


def create_course(request):
    courses=Course.objects.all()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            instance = form.save()
            # Redirect to a success page or do other processing
            return redirect('SearchMovie')
    else:
        form = CourseForm()
    
    return render(request, 'create_course.html', {'form': form, 'courses':courses})

# def deleteCourse(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
#     course.delete()
    
#     return redirect('create_course', course.id)
def show_course(request):
    courses=Course.objects.all()
    return render(request, 'Show_courses.html', {'courses':courses})