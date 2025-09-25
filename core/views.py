from django.shortcuts import render, redirect
from django.contrib import messages
from courses.models import Course
from .models import Message as ContactMessage
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

def home(request):
    """Home page view"""
    featured_courses = Course.objects.filter(is_active=True)[:3]
    context = {
        'featured_courses': featured_courses,
    }
    return render(request, 'core/home.html', context)

def about(request):
    """About page view"""
    return render(request, 'core/about.html')

def contact(request):
    """Contact page view"""
    if request.method == 'POST':
        name = request.POST.get('name') or ''
        email = request.POST.get('email') or ''
        subject = request.POST.get('subject') or ''
        body = request.POST.get('message') or ''

        if name and email and body:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=body,
            )
            messages.success(request, f'Thank you {name}! Your message has been sent successfully.')
            return redirect('core:contact')
        else:
            messages.error(request, 'Please fill in your name, email, and message.')

    return render(request, 'core/contact.html')


def terms(request):
    """Terms & Conditions page view"""
    return render(request, 'core/terms.html')


def _is_staff(user):
    return user.is_authenticated and user.is_staff


@user_passes_test(_is_staff)
def messages_dashboard(request):
    """Staff-only dashboard to view contact messages"""
    qs = ContactMessage.objects.all()
    # Optional filters or mark-as-read can be added later
    context = {"messages_list": qs}
    return render(request, 'core/messages_dashboard.html', context)