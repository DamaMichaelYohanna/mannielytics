from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from courses.models import Course
from courses.forms import CourseForm
from core.models import Message

def admin_login(request):
    """Admin login view"""
    if request.user.is_authenticated:
        return redirect('dashboard:manage_courses')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_staff:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('dashboard:manage_courses')
            else:
                messages.error(request, 'Invalid credentials or insufficient permissions.')
        else:
            messages.error(request, 'Invalid form data.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'dashboard/login.html', {'form': form})

@login_required
def admin_logout(request):
    """Admin logout view"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('core:home')

@login_required
def manage_courses(request):
    """Course management dashboard"""
    if not request.user.is_staff:
        messages.error(request, 'Access denied. Staff privileges required.')
        return redirect('core:home')
    
    courses = Course.objects.all().order_by('-created_at')
    context = {
        'courses': courses,
    }
    return render(request, 'dashboard/manage_courses.html', context)


@login_required
def messages_list(request):
    """Staff-only list of contact messages"""
    if not request.user.is_staff:
        messages.error(request, 'Access denied. Staff privileges required.')
        return redirect('core:home')

    msgs = Message.objects.all()
    context = { 'messages_list': msgs }
    return render(request, 'dashboard/messages.html', context)

@login_required
def add_course(request):
    """Add new course"""
    if not request.user.is_staff:
        messages.error(request, 'Access denied. Staff privileges required.')
        return redirect('core:home')
    
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course added successfully!')
            return redirect('dashboard:manage_courses')
    else:
        form = CourseForm()
    
    context = {
        'form': form,
        'action': 'Add'
    }
    return render(request, 'dashboard/course_form.html', context)

@login_required
def edit_course(request, pk):
    """Edit existing course"""
    if not request.user.is_staff:
        messages.error(request, 'Access denied. Staff privileges required.')
        return redirect('core:home')
    
    course = get_object_or_404(Course, pk=pk)
    
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course updated successfully!')
            return redirect('dashboard:manage_courses')
    else:
        form = CourseForm(instance=course)
    
    context = {
        'form': form,
        'action': 'Edit',
        'course': course
    }
    return render(request, 'dashboard/course_form.html', context)

@login_required
def delete_course(request, pk):
    """Delete course"""
    if not request.user.is_staff:
        messages.error(request, 'Access denied. Staff privileges required.')
        return redirect('core:home')
    
    course = get_object_or_404(Course, pk=pk)
    course_title = course.title
    course.delete()
    messages.success(request, f'Course "{course_title}" deleted successfully!')
    return redirect('dashboard:manage_courses')
