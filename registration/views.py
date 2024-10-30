from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect

from .import forms

def register(request):
    if request.method == "POST":
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect("homepage")
    else:
        register_form = forms.RegistrationForm()
    return render(request,'register.html',{'form':register_form})
