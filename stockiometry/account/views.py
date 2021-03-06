from django.shortcuts import render
from account.forms import UserForm,UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here.



def index(request):
    return HttpResponse("Welcome")


def user_register(request):

    registered = False

    user_form = UserForm(data=request.POST or None)
    profile_form = UserProfileInfoForm(data=request.POST or None)

    if request.method=='POST':


        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)

            profile.user = user

            profile.save()

            registered = True

        else:
             print(user_form.errors,profile_form.errors)


    return render(request,"templates/register.html",{'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})




def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(username=username, password=password)

        request.session['username'] = username


        if user:

            if user.is_active:

                request.session['username'] = username

                print(request.session['username'])

                login(request,user)

                return HttpResponseRedirect(reverse('stockapp:home'))
            else:

                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'templates/login.html', {})
