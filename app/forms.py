from django import forms
from django.core.validators import RegexValidator

from .models import Candidate

# every letters to LowerCase
class LowerCase(forms.CharField):
    def to_python(self, value):
        return value.lower()

# every letters to UpperCase
class UpperCase(forms.CharField):
    def to_python(self, value):
        return value.upper()


class CandidateForm(forms.ModelForm):

    # VALIDATION
    firstname = forms.CharField(
        label='First Name', min_length=3, max_length=50, 
        validators=[RegexValidator(r'^[a-zA-Z\s-]*$', 
        message='Only letters is allowed !')], 
        widget=forms.TextInput(attrs={'placeholder': 'Input your first name'})
    )

    lastname = forms.CharField(
        label='Last Name', min_length=3, max_length=50, 
        validators=[RegexValidator(r'^[a-zA-Z\s]*$', 
        message='Only letters is allowed !')], 
        widget=forms.TextInput(attrs={'placeholder': 'Input your Last name'})
    )

    job = UpperCase(
        label='Job Code',
        min_length=5,
        max_length=5,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Examples: RF-22',
            }
        )
    )

    email = LowerCase(
        label='Email Address', min_length=10, max_length=50, 
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', 
        message='Put a valid email address !')], 
        widget=forms.TextInput(attrs={'placeholder': 'Input your Email'})
    )

    
    # method 2
    # age = forms.CharField(
    #     label='Age', 
    #     validators=[RegexValidator(r'^[0-9]*$', 
    #     message='Only numbers is allowed !')], 
    #     widget=forms.TextInput(attrs={'placeholder': 'Your Age'})
    #     )

    age = forms.IntegerField(
        label='Age', max_value=200,
        # validators=[RegexValidator(r'^[0-9]*$', 
        # message='Only numbers is allowed !')], 
        widget=forms.NumberInput(attrs={'placeholder': 'Your Age'}),
        # required=False
    )

    messages = forms.CharField(
        label='About you', 
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': 'Talk a little about you .', 'rows':5}
            # 'rows':5 限制textarea行數
        ),         
    )

    class Meta:
        model = Candidate
        fields = '__all__'
        # fields = ['firstname', 'lastname', 'email', 'age', 'messages']
        # exclude = ['firstname', 'lastname', 'email', 'age', 'messages']

        # Outside widget
        widgets = {
            'phone':forms.TextInput(
                attrs={
                    'style':'font-size:13px', #CSS
                    'placeholder': 'Your phone number .',
                    'data-mask':'(00) 0000-0000',
                }
            )
        }