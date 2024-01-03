from django.shortcuts import render
from core.models import Student
# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):

    return render(request, 'about.html')

def view_student(request):
    student = Student.objects.all()
    context = {
        'student':student,
    }
    return render(request, 'view.html',context)