from django.shortcuts import render, redirect
from .models import Course

def course_list(request):
    
    courses = Course.objects.all()
    
    return render(request, 'courses/list.html', {'courses': courses})

def add_course(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        duration = request.POST.get('duration', '').strip()
        
        if title and duration:
            Course.objects.create(title=title, duration=duration)
            return redirect('course_list')

    
    return render(request, 'courses/add.html')

