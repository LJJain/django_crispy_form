from django import forms

from .models import Candidates

class CandidatesForm(forms.ModelForm):
    class Meta:
        model=Candidates
        fields= ['firstname', 'lastname', 'email', 'messages']