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
    ('Laravel', 'Laravel'),
    ('Angular', 'Angular'),
    ('Dango', 'Dango'),
    ('Flask', 'Flask'),
    ('Vue', 'Vue'),
    ('Others', 'Others'),
)

LANGUAGES = (
    ('Python', 'Python'),
    ('Java', 'Java'),
    ('Javascript', 'Javascript'),
    ('C++', 'C++'),
    ('Ruby', 'Ruby'),
    ('Others', 'Others'),
)

DATABASES = (
    ('MySQL', 'MySQL'),
    ('Postgree', 'Postgree'),
    ('MongoDB', 'MongoDB'),
    ('SqLite3', 'SqLite3'),
    ('Oracle', 'Oracle'),
    ('Others', 'Others'),
)

LIBRARIES = (
    ('Ajax', 'Ajax'),
    ('Jquery', 'Jquery'),
    ('React.js', 'React.js'),
    ('Chart.js', 'Chart.js'),
    ('Gsap', 'Gsap'),
    ('Others', 'Others'),
)

MOBILE = (
    ('React native', 'React native'),
    ('Kivy', 'Kivy'),
    ('Flutter', 'Flutter'),
    ('Ionic', 'Ionic'),
    ('Xamarim', 'Xamarim'),
    ('Others', 'Others'),
)

OTHERS = (
    ('UML', 'UML'),
    ('SQL', 'SQL'),
    ('Docker', 'Docker'),
    ('GIT', 'GIT'),
    ('GraphQL', 'GraphQL'),
    ('Others', 'Others'),
)

# EDUCATION
STATUS_COURSE = (
    ('', 'Select your status'),
    ('Studying', 'Studying'),
    ('Break', 'Break'),
    ('Completed', 'Completed'),
)



class Candidate(models.Model):
    # PERSONAL (CARD 1)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    job = models.CharField(max_length=5, null=True, blank=True, verbose_name='Job Code')
    email = models.EmailField(max_length=50)
    # age = models.IntegerField(null=True)
    birth = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Birthday', null=True)
    phone = models.CharField(max_length=20, null=True)

    personality = models.CharField(max_length=50, null=True, choices=PERSONALITY)
    salary = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=10, null=True)
    experience = models.BooleanField(null=True)
    smoker = models.CharField(max_length=10, null=True, choices=SMOKER, default="")

    messages = models.TextField(verbose_name='Presentation')

    file = models.FileField(upload_to='resume', blank=True, verbose_name='Resume')
    image = models.ImageField(upload_to='photo', blank=True, verbose_name='Photo')

    Situation = models.CharField(max_length=100, null=True, choices=SITUATION, default='Pending')
    created = models.DateTimeField(auto_now_add=True)

    company_note = models.TextField(blank=True)
    
    # SKILLS (CARD 2)
    # Multiple Checkboxes
    frameworks = MultiSelectField(max_length=50, choices=FRAMEWORKS, default="")
    languages = MultiSelectField(max_length=50, choices=LANGUAGES, default="")
    databases = MultiSelectField(max_length=50, choices=DATABASES, default="")
    libraries = MultiSelectField(max_length=50, choices=LIBRARIES, default="")
    mobile = MultiSelectField(max_length=50, choices=MOBILE, default="")
    others = MultiSelectField(max_length=50, choices=OTHERS, default="")

    # EDUCATION (CARD 3)
    institution = models.CharField(max_length=50, null=True)
    course = models.CharField(max_length=50, null=True)
    started_course = models.DateField(auto_now_add=False, auto_now=False, null=True)
    finished_course = models.DateField(auto_now=False, auto_now_add=False, null=True)
    about_course = models.TextField(null=True)
    status_course = models.CharField(max_length=50, null=True, choices=STATUS_COURSE)

    # PROFESSIONAL (CARD 4)
    company = models.CharField(max_length=50, null=True)
    position = models.CharField(max_length=50, null=True)
    started_job = models.DateField(auto_now_add=False, auto_now=False,null=True)
    finished_job = models.DateField(auto_now=False, auto_now_add=False, null=True)
    about_job = models.TextField(max_length=200, null=True)
    employed = models.BooleanField(null=True, verbose_name="I am employed .")
    remote = models.BooleanField(null=True, verbose_name="I agree to work remotly")
    travel = models.BooleanField(null=True, verbose_name="I'm available for travel")
    
    # Capitalize the first and last name
    def clean(self):
        self.firstname = self.firstname.capitalize()
        self.lastname = self.lastname.capitalize()

    def __str__(self):
        return self.firstname

    # Concatenate F-name+L-name (Admin-Table)
    def name(obj):
        return "%s %s" % (obj.firstname, obj.lastname)

    # Concatenate (When clicking over the candidates)
    def __str__(self):
        return self.firstname+" "+self.lastname

