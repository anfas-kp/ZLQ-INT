from django.shortcuts import render, redirect, get_object_or_404
from .models import Student


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})


def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        age = request.POST.get('age')
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        course = request.POST.get('course', '').strip()
        address = request.POST.get('address', '').strip()

        Student.objects.create(
            name=name,
            age=age,
            email=email or None,
            phone=phone or None,
            course=course or None,
            address=address or None,
        )
        return redirect('student_list')

    return render(request, 'students/add.html')


def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
    return redirect('student_list')
