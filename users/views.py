#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import PatientSignupForm, DoctorSignupForm
from .models import CustomUser

def signup(request):
    return render(request, 'users/signup.html')

def patient_signup(request):
    if request.method == 'POST':
        form = PatientSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('patient_dashboard')
    else:
        form = PatientSignupForm()
    return render(request, 'users/patient_signup.html', {'form': form})

def doctor_signup(request):
    if request.method == 'POST':
        form = DoctorSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('doctor_dashboard')
    else:
        form = DoctorSignupForm()
    return render(request, 'users/doctor_signup.html', {'form': form})

def patient_dashboard(request):
    return render(request, 'users/patient_dashboard.html')

def doctor_dashboard(request):
    return render(request, 'users/doctor_dashboard.html')
