from django.shortcuts import render, redirect
from .models import Student


def home(request):

    if request.method == 'POST':

        name = request.POST['name']
        age = request.POST['age']
        course = request.POST['course']

        Student.objects.create(
            name=name,
            age=age,
            course=course
        )

        return redirect('/')

    students = Student.objects.all()

    return render(
        request,
        'home.html',
        {'students': students}
    )


def delete_student(request, id):

    student = Student.objects.get(id=id)

    student.delete()

    return redirect('/')