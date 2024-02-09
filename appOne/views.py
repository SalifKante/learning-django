from django.shortcuts import render
from appOne.models import Topic, Webpage, AccessRecord, User
from . import forms
from appOne.forms import UserPracticeForm, UserForm, UserProfileInfoForm

#
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    content_dic = {'filter_text': 'Hello World', 'filter_number':100}
    return render(request, 'app_one/index.html', context=content_dic)


def record_list(request):
    webpages_list = AccessRecord.objects.order_by('date')
    my_dict = {'access_records':webpages_list}
    return render(request, 'app_one/record_list.html',context=my_dict)

def get_user(request):
    users = User.objects.all()
    mydict = {'user_records': users}
    return render(request, 'app_one/user.html', context=mydict)

def create_user(request):
    form = UserPracticeForm()

    if request.method == "POST":
        form = UserPracticeForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            """print("VALIDATION SUCCESS!")
            print("FIRST NAME:" + form.cleaned_data['first_name'])
            print("LAST NAME:" + form.cleaned_data['last_name'])
            print("EMAIL:" + form.cleaned_data['email'])"""
            return render(request, 'app_one/index.html')
        else:
            print("Error Form Invalid")
    
    return render(request, 'app_one/create_user.html', {'form':form})



def form_name_view(request):
    form = forms.FormName

    if request.method == 'POST':

        form = forms.FormName(request.POST)
        if form.is_valid():
            #DO SOMETHING
            print("VALIDATION SUCCESS!")
            print("NAME:" + form.cleaned_data['name'])
            print("EMAIL:" + form.cleaned_data['email'])
            print("TEXT:" + form.cleaned_data['text'])

    my_form = {'form':form}
    return render(request, 'app_one/form_page.html', context=my_form)

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()

            registered = True
            
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    
    return render(request, 'app_one/registration.html',{'user_form':user_form, 'profile_form':profile_form,'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account Not Active')
        else:
            print("Someone tried to login and failed")
            print("Username: {} and Password: {}".format(username, password))
            return HttpResponse('Invalid login details supplied!')
    else:
        return render(request, 'app_one/login.html',{})

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
