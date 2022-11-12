from django.db import models

from multiselectfield import MultiSelectField
# from ckeditor.fields import RichTextField

# Create your models here.

SITUATION = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Disapproved', 'Disapproved'),
)

PERSONALITY = (
    ('', 'Select your personality'),
    ('I am Outgoing', 'I am Outgoing'),
    ('I am Sociable', 'I am Sociable'),
    ('I am Antisociable', 'I am Antisociable'),
    ('I am Discreet', 'I am Discreet'),
    ('I am Seriou', 'I am Seriou'),
)

SMOKER = (
    ('1', 'Yes'),
    ('2', 'No'),
)

# Multiple Checkboxes
FRAMEWORKS = (
    # ('Laravel', 'Laravel'),
    ('Angular', 'Angular'),
    ('Dango', 'Dango'),
    ('Flask', 'Flask'),
    ('Vue', 'Vue'),
    ('Others', 'Others'),
)



class Candidate(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    job = models.CharField(max_length=5, null=True, blank=True)
    email = models.EmailField(max_length=50)
    age = models.IntegerField(null=True)
    phone = models.CharField(max_length=20, null=True)

    personality = models.CharField(max_length=50, null=True, choices=PERSONALITY)
    salary = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=10, null=True)
    experience = models.BooleanField(null=True)
    smoker = models.CharField(max_length=10, null=True, choices=SMOKER, default="")

    messages = models.TextField()

    file = models.FileField()

    Situation = models.CharField(max_length=100, null=True, choices=SITUATION, default='Pending')
    created = models.DateTimeField(auto_now_add=True)

    # Multiple Checkboxes
    frameworks = MultiSelectField(max_length=50, choices=FRAMEWORKS, default="")
    
    # Capitalize the first and last name
    def clean(self):
        self.firstname = self.firstname.capitalize()
        self.lastname = self.lastname.capitalize()

    def __str__(self):
        return self.firstname