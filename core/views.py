from django.shortcuts import render, redirect  # i added redirect
# i imported authenticate for sign up, down here
from django.contrib.auth.models import User, auth
from django.contrib import messages  # import for error message
from django.http import HttpResponse
# this import checks of user entered the page
from django.contrib.auth.decorators import login_required
from .models import Profile  # i imported Profile class

# Create your views here.


@login_required(login_url='signin')  # user cannot access directly to main menu
def index(request):
    return render(request, 'index.html')


@login_required(login_url='signin')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':

        if request.FILES.get('image'):
            image = user_profile.profileimg
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()

            return redirect('settings')

    return render(request, 'setting.html', {'user_profile': user_profile})


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
                user_login = auth.authenticate(
                    username=username, password=password)
                # user if logged in clearly , user do it whatever you want (ex:settings) down here code
                auth.login(request, user_login)

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


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')

    else:
        return render(request, 'signin.html')


def logout(request):
    auth.logout(request)
    return redirect('signin')
