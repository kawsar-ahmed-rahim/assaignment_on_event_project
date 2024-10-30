from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        #fields = ['name','category','date','location','description']
        fields = '__all__'
    date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))


class EventForm2(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name','date','location','description']
    


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
        