from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout




def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = user_name,password = user_pass)
            if user is not None:
                login(request,user)
                return redirect('homepage')
            else:
                return redirect('register')
    else:
        form = AuthenticationForm()
    return render(request,'login_logout.html',{'form':form,'type':'Login'})

def user_logout(request):
    logout(request)
    return redirect('user_login')
