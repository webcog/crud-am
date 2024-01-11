from django.shortcuts import render, redirect, get_object_or_404
from core.models import Student
# Create your views here.

def index(request):
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        father_name = request.POST.get('father_name')
        roll_no = request.POST.get('roll_no')
        phone_no = request.POST.get('phone_no')
        postal_code = request.POST.get('postcode')


        student = Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            father_name=father_name,
            roll_no=roll_no,
            phone_no=phone_no,
            postal_code=postal_code
        )
        return redirect('view')


    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def view_student(request):
    student = Student.objects.all().order_by('-id')
    context = {
        'student':student,
    }
    return render(request, 'view.html',context)


def updatestudent(request, id):
    student = get_object_or_404(Student,id=id)
    if request.method == "POST":
        student.first_name = request.POST.get('fname')
        student.last_name = request.POST.get('lname')
        student.father_name = request.POST.get('father_name')
        student.roll_no = request.POST.get('roll_no')
        student.phone_no = request.POST.get('phone_no')
        student.postal_code = request.POST.get('postcode')
        student.save()

    context = {
        'student':student,
    }
    
    return render(request, 'update.html', context)