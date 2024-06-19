from django import forms
from .models import Candidate, Vote

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['name', 'surname', 'party', 'age']

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['voter_name', 'voter_surname']

class CustomAuthenticationForm(forms.Form):
    custom_username = forms.CharField(label='Custom Username', max_length=254, widget=forms.TextInput(attrs={'class': 'form-control'}))
    custom_password = forms.CharField(label='Custom Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
