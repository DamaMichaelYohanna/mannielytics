from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Course

# Create your views here.

class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'
    paginate_by = 9
    
    def get_queryset(self):
        return Course.objects.filter(is_active=True)

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'
    
    def get_queryset(self):
        return Course.objects.filter(is_active=True)
