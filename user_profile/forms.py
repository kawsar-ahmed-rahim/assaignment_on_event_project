from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

"""class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['mobile_number','address','website']
        widgets = {
            'mobile_number':forms.TextInput(attrs={'placeholder':'Mobile Phone'}),
            'address':forms.Textarea(attrs={'placeholder':'Address','rows':3}),
            'website':forms.TextInput(attrs={'placeholder':'website'})}"""
               