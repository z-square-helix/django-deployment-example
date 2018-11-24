from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from example_app.models import Topic, Webpage, AccessRecord, Userinos
from . import forms
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records' : webpages_list}

    return render(request, 'example_app/index.html', context = date_dict)

def users(request):
    user_list = Userinos.objects.order_by('first_name')
    usr_dict = {'users' : user_list}

    return render(request, 'example_app/users.html', context = usr_dict)

def forms_view(request):
    form = forms.FormName()

    if request.method == 'post':
        form = forms.FormName(request.POST)

        if form.is_valid():
            #This code will do something with the data
            print('NAME: ' + form.cleaned_data['name'])
            print('EMAIL: ' + form.cleaned_data['email'])
            print('TEXT: ' + form.cleaned_data['text'])


    return render(request, 'example_app/forms.html', {'form': form})

def signup_form(request):
    sup_form = forms.SignUp()

    if request.method == 'POST':
        sup_form = forms.SignUp(request.POST)

        if sup_form.is_valid():
            sup_form.save()
            return index(request)

        else:
            print('ERROR FORM INVALID')

    return render(request, 'example_app/signup.html', {'sup_form' : sup_form})

def relative(request):
    return render(request, 'example_app/relative_url.html')

def child(request):
    context_dict = {'text' : 'hello world', 'number' : 5280}

    return render(request, 'example_app/child.html', context = context_dict)

def register(request):

    registered = False

    if request.method == "POST":
        user_form = forms.UserForm(data = request.POST)
        profile_form = forms.UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user.form.errors, profile_form.errors)

    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()

    return render(request, 'example_app/registration.html',
                    {'user_form':user_form,
                    'profile_form':profile_form,
                    'registered':registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('example_app:index'))

            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')

        else:
            print('someone tried to login and failed')
            print('Username: {} and password {}'.format(username, password))
            return HttpResponse('INVALID LOGIN DETAILS SUPPLIED')

    else:
        return render(request, 'example_app/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('example_app:index'))
