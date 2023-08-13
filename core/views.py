from django.shortcuts import render, redirect  # i added redirect
# i imported authenticate for sign up, down here
from django.contrib.auth.models import User, auth
from django.contrib import messages  # import for error message
from django.http import HttpResponse
from .models import Profile  # i imported Profile class

# Create your views here.


def index(request):
    return render(request, 'index.html')


def signup(request):  # request parameter means call http file
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']  # i wrote input name=''
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username already taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,
                                                email=email,
                                                password=password)
                user.save()

                # log user in and rediret to settings page (i'm gonna add later)

                # create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model,
                                                     id_user=user_model.id)
                new_profile.save()
                return redirect('signup')
        else:
            messages.info(request, 'password not matching')
            return redirect('signup')

    else:
        return render(request, 'signup.html')
