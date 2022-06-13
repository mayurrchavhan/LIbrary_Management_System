from django.shortcuts import render, redirect
from .models import Student
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout successful')
    return redirect('home')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(request,
                                 username=request.POST['EmailID'],
                                 password=request.POST['password'])
        print(user)
        if user is None:
            messages.error(request, 'Invalid CREDENTIALS')
            return redirect('/student/login/')
        else:
            auth.login(request, user)
            messages.success(request, 'Login successful')
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            return redirect('home')
    else:
        return render(request, 'student/login.html')


def signup(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(username=request.POST['EmailID'])
            messages.success(request, 'user exists already !!')
            return redirect('/student/login/')

        except User.DoesNotExist:
            user = User.objects.create_user(username=request.POST['EmailID'], password=request.POST['password'])

            newstudent = Student.objects.create(first_name=request.POST['firstname'],
                                                last_name=request.POST['lastname'],
                                                student_id=user
                                                )

            auth.login(request, user)
            messages.success(request, 'Signup successful')
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('home')

    else:
        return render(request, 'student/signup.html', {
            "users": list(User.objects.values_list('username', flat=True))
        })
