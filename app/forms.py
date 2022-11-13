from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

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
        error_messages= {'required':'First Name Can Not Be Empty !',},
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Input your First name',
                'style': 'font-size: 15px; text-transform: capitalize', #只會影響前端輸入
            },
        )
    )

    lastname = forms.CharField(
        label='Last Name', min_length=3, max_length=50, 
        validators=[RegexValidator(r'^[a-zA-Z\s]*$', 
        message='Only letters is allowed !')], 
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Input your Last name',
                'style': 'font-size: 15px; text-transform: capitalize',
            },
        )
    )

    # job allways in Uppercase
    job = UpperCase(
        label='Job Code',
        min_length=5,
        max_length=5,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Examples: RF-22',
                'style': 'font-size: 15px; text-transform: uppercase',
                'data-mask': 'AA-00',
            }
        )
    )

    # email allways in Lowercase
    email = LowerCase(
        label='Email Address', min_length=10, max_length=50, 
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', 
        message='Put a valid email address !')], 
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Input your Email',
                'style': 'font-size: 15px; text-transform: lowercase',
            }
        )
    )

    
    # method 2
    # age = forms.CharField(
    #     label='Age', 
    #     validators=[RegexValidator(r'^[0-9]*$', 
    #     message='Only numbers is allowed !')], 
    #     widget=forms.TextInput(attrs={'placeholder': 'Your Age'})
    #     )

    # Age
    # age = forms.IntegerField(
    #     label='Age', max_value=200,
    #     # validators=[RegexValidator(r'^[0-9]*$', 
    #     # message='Only numbers is allowed !')], 
    #     widget=forms.NumberInput(attrs={'placeholder': 'Your Age'}),
    #     # required=False
    # )

    # Checkbox
    experience = forms.BooleanField(
        label='I have experience',
        required=False,
    )

    # Messages
    messages = forms.CharField(
        label='About you', 
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': 'Talk a little about you .', 'rows':5}
            # 'rows':5 限制textarea行數
        )         
    )

    # File (Upload resume)
    file = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                'style': 'font-size: 13px;',
                # method 1 
                # 'accept': 'application/pdf, application/msword, application/vnd.openxmlformats-officedocument.wordprcessingml.document',
            }
        )
    )

    # Image (Upload photo)
    image = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                'style': 'font-size: 13px;',
                'accept': 'image/png, image/jepg',
            }
        )
    ) 

    # Institution
    institution = forms.CharField(
        label= 'Institution',
        min_length=3, 
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'style': 'font-size: 13px;',
                'placeholder': 'Institution Name',
            }
        )
    )

    # Course
    institution = forms.CharField(
        min_length=3, 
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'style': 'font-size: 13px;',
                'placeholder': 'Your Course',
            }
        )
    )

    # about_course
    about_course = forms.CharField(
        label='About your Course', 
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Talk a little about you .',
                'style': 'font-size: 13px;',
                'rows':5, # 'rows':5 限制textarea行數
            }
        )         
    )

    # about_job
    about_job = forms.CharField(
        label='About your Course', 
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Talk a little about you .',
                'style': 'font-size: 13px;',
                'rows':5, # 'rows':5 限制textarea行數
            }
        )         
    )

    # Company (Last Company)
    company = forms.CharField(
        label= 'Last Company', 
        required=False,
        min_length=3,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Company Name',
                'style': 'font-size: 13px;',
            }
        )
    )

    # Position
    position = forms.CharField(
        label= 'Last Company', 
        required=False,
        min_length=3,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your Occupation',
                'style': 'font-size: 13px;',
            }
        )
    )

    employed = forms.BooleanField(label='I am employed .', required=False)
    remote = forms.BooleanField(label='I agree to work remotly', required=False)
    travel = forms.BooleanField(label='I am available for travel', required=False)

    # method 1 (Gender)
    # GENDER = [('M', 'Male'), ('F', 'Female'),]
    # gender = forms.CharField(
    #     label='Gender', 
    #     widget=forms.RadioSelect(
    #         choices=GENDER
    #     )
    # )
    
    class Meta:
        model = Candidate
        # fields = '__all__'
        # fields = ['firstname', 'lastname', 'email', 'age', 'messages']
        exclude = ['created', 'Situation']

        # Label control
        labels = {
            'started_course':'Start',
            'finished_course':'Finished',
            'started_job':'Start',
            'finished_job':'Finished',
        }

        SALARY = (
            ('', 'Salary Expectation (per month)'),
            ('Between ($3000 - $4000)', 'Between ($3000 - $4000)'),
            ('Between ($4000 - $5000)', 'Between ($4000 - $5000)'),
            ('Between ($5000 - $7000)', 'Between ($5000 - $7000)'),
            ('Between ($7000-10000)', 'Between ($7000-10000)'),
        )

        # method 2 (Gender)
        GENDER = [('M', 'Male'), ('F', 'Female'),]

        # OUTSIDE WIDGETS
        widgets = {
            # Birth date
            'birth':forms.DateInput(
                attrs={
                    'style':'font-size:13px; cursor: pointer', #CSS
                    'type': 'date',
                    'onkeydown': 'return false',    #Block typing inside the input
                    'min': '1900-01-01',
                    'max': '2100-12-31',
                }
            ),

            # started_course
            'started_course':forms.DateInput(
                attrs={
                    'style':'font-size:13px; cursor: pointer', #CSS
                    'type': 'date',
                    'onkeydown': 'return false',    #Block typing inside the input
                    'min': '1900-01-01',
                    'max': '2100-12-31',
                }
            ),

            # finished_course
            'finished_course':forms.DateInput(
                attrs={
                    'style':'font-size:13px; cursor: pointer', #CSS
                    'type': 'date',
                    'onkeydown': 'return false',    #Block typing inside the input
                    'min': '1900-01-01',
                    'max': '2100-12-31',
                }
            ),

            # started_job
            'started_job':forms.DateInput(
                attrs={
                    'style':'font-size:13px; cursor: pointer', #CSS
                    'type': 'date',
                    'onkeydown': 'return false',    #Block typing inside the input
                    'min': '1900-01-01',
                    'max': '2100-12-31',
                }
            ),

            # finished_job
            'finished_job':forms.DateInput(
                attrs={
                    'style':'font-size:13px; cursor: pointer', #CSS
                    'type': 'date',
                    'onkeydown': 'return false',    #Block typing inside the input
                    'min': '1900-01-01',
                    'max': '2100-12-31',
                }
            ),

            # Phone
            'phone':forms.TextInput(
                attrs={
                    'style':'font-size:13px', #CSS
                    'placeholder': 'Your phone number .',
                    'data-mask':'(00) 0000-0000',
                    'autocomplete': 'off',
                }
            ),

            # Salary
            'salary':forms.Select(
                choices = SALARY,
                attrs={
                    'class':'form-control', #Boostrap inside the forms.py
                }
            ),

            # Gender
            'gender':forms.RadioSelect(
                choices = GENDER,
                attrs={
                    'class':'btn-check', #Boostrap
                }
            ),

            # Smoker
            'smoker':forms.RadioSelect(
                # 選項已在models.py建立
                attrs={
                    'class':'btn-check', #Boostrap
                }
            ),
        }

    # 'SUPER' FUNCTIONS
    def __init__(self, *args, **kwargs):
        super(CandidateForm, self).__init__(*args, **kwargs)

        # ================ CONTROL PANEL (individual <Inputs> ) ================
        # 1) INPUT REQUIRED
        # self.fields["messages"].required = True

        # 2) INPUT DISABLE
        # self.fields['experience'].disabled = True

        # 3) INPUT READONLY
        # self.fields['email'].widget.attrs.update({'readonly':'readonly'})
        
        # 4) SELECT OPTION 
        # self.fields["personality"].choices = [('', 'Select your personality'),] + list(self.fields["personality"].choices)[1:]
        # self.fields["status_course"].choices = [('', 'Select your status'),] + list(self.fields["status_course"].choices)[1:]

        # 5) WEDGETS (inside/outside)
        # self.fields['phone'].widget.attrs.update(
        #     {
        #        'style':'font-size:13px', 
        #        'placeholder': 'Your phone number .',
        #        'data-mask':'(00) 0000-0000',
        #     }
        # )

        # 6) ERROR MESSAGES
        # self.fields['lastname'].error_messages.update(
        #     {
        #         'required': 'Last Name Can Not Be Empty !'
        #     }
        # )

        # ================ ADVANCED CONTROL PANEL (multiple <Inputs>)| READONLY/DISABLE | BY 'LOOP FOR' IN [ARRAY]  ================
        # 1) READONLY
        # readonly = ['firstname', 'lastname', 'job']
        # for field in readonly:
        #     self.fields[field].widget.attrs['readonly'] = 'true'

        # 2) DISABLE
        # disabled = ['personality', 'salary', 'gender', 'smoker']
        # for field in disabled:
        #     self.fields[field].widget.attrs['disabled'] = 'true'

        # 3) ERROR MESSAGES
        # error_messages = ['email', 'phone', 'age']
        # for field in error_messages:
        #     self.fields[field].error_messages.update(
        #         {
        #             'required': 'Can Not Be Empty',
        #         }
        #     )

        # 4) FONT SIZE
        # font_size = ['email', 'phone', 'age']
        # for field in font_size:
        #     self.fields[field].widget.attrs.update(
        #         {
        #             'style':'font-size: 13 px',
        #         }
        #     )
    #======================= END SUPER FUNCTIONS =========================|

    # ================== FUNCTION (METHOD CLEAN) ===========================| 
    # ==================1. FUNCTIONS TO PREVENT DUPLICATED ENTRIES =========|
    # METHOD 1 (LOOP FOR)
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     for obj in Candidate.objects.all():
    #         if obj.email == email:
    #             raise forms.ValidationError('Denied ! ' + email + ' is already registered !')
    #     return email

    # METHOD 2 (if statement w/ filter)
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Candidate.objects.filter(email=email).exists():
            raise forms.ValidationError('Denied ! {} is already registered !'.format(email))
        return email

    # ================== 2. JOB CODE (JOB CODE VALIDATION) =========|
    def clean_job(self):
        job = self.cleaned_data.get('job')
        if job == 'FR-22' or job == 'BA-10' or job=='FU-15':
            return job
        else:
            raise forms.ValidationError('This Code is Invalid !')

    # ================== 3. Age (Range: 18-65) =========|
    # def clean_age(self):
    #     age = self.cleaned_data.get('age')
    #     if age < 18 or age > 65:
    #         raise forms.ValidationError('Age must be between 18 and 65')
    #     return age

    # ================== 4. Phone (Prevent incomplete values) =========|
    # def clean_phone(self):
    #     phone = self.cleaned_data.get('phone')
    #     if len(phone) != 10:
    #         raise forms.ValidationError('Wrong phone number !')
    #     return phone

    # ================== 5. RESTRICTION (File extensions - method 2) =========|
    def clean_file(self):
        file = self.cleaned_data('file')
        content = file.content
        if content == 'application/pdf' or content == 'application/msword' :
            return file
        else:
            raise forms.ValidationError('Only PDF,DOC and DOCX')

