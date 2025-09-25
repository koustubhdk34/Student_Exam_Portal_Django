from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Student, Exam, Registration
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        whatsapp = request.POST.get('whatsapp', '')
        country = request.POST['country']
        address = request.POST['address']

        user = User.objects.create_user(username=username, email=email, password=password)
        Student.objects.create(user=user, phone=phone, whatsapp=whatsapp, country=country, address=address)
        return redirect('login')

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
        except User.DoesNotExist:
            pass
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def exams(request):
    exams_list = Exam.objects.all()
    if request.method == 'POST':
        exam_id = request.POST['exam_id']
        student = request.user.student
        exam = Exam.objects.get(id=exam_id)
        Registration.objects.create(student=student, exam=exam)
        return redirect('dashboard')
    return render(request, 'exams.html', {'exams': exams_list})

from django.contrib.auth.decorators import login_required

@login_required
def results(request):
    student = request.user.student  # this is safe now because only logged-in users reach here
    regs = Registration.objects.filter(student=student)
    return render(request, 'results.html', {'registrations': regs})
