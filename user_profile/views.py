from django.shortcuts import render,redirect
from .import forms
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

"""def add_profile(request):
    if request.method == "POST":
        profile_form = forms.ProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect("add_profile")
    else:
        profile_form = forms.ProfileForm()
    return render(request,'add_profile.html',{'form':profile_form ,})"""
@login_required
def add_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('add_profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request,'add_profile.html',{'form':form})
    
