from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib import messages
from  f_app.forms import RegisterForm,ChangeUserData 
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'home.html')

def SignUp(request):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Account Created Successfully!')
        else :
            form = RegisterForm()
        return render(request,'signup.html',{'form':form})


def user_login(request):
        if request.method == 'POST':
            form = AuthenticationForm(request = request ,data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username = name ,password = upass)
                if user is not None :
                    messages.success(request, "Logged in Successfully")
                    login(request,user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request,'login.html',{'form':form})
   
@login_required(login_url='login')
def Profile(request):
     return render(request,'profile.html')

@login_required(login_url='login')
def User_logout(request):
    logout(request)
    messages.warning(request, "Logged out Successfully")
    return redirect('login')

@login_required(login_url='login')
def passchng(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user = request.user ,data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password has been updated')
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else :
        form = PasswordChangeForm(user = request.user)
    return render(request,'chngpass1.html',{'form':form})
        
@login_required(login_url='login')
def passchngWO(request):
    if request.method == 'POST':
        form = SetPasswordForm(user = request.user,data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password has been updated')
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form = SetPasswordForm(user = request.user)
    return render(request,'chngpass2.html',{'form':form})