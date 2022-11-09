from django.db import models

# Create your models here.

SITUATION = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Disapproved', 'Disapproved'),
)

class Candidate(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    job = models.CharField(max_length=5, null=True, blank=True)
    email = models.EmailField(max_length=50)
    age = models.IntegerField(null=True)
    phone = models.CharField(max_length=20, null=True)
    messages = models.TextField()
    Situation = models.CharField(max_length=100, null=True, choices=SITUATION, default='Pending')

    created = models.DateTimeField(auto_now_add=True)
    
    # Capitalize the first and last name
    def clean(self):
        self.firstname = self.firstname.capitalize()
        self.lastname = self.lastname.capitalize()

    def __str__(self):
        return self.firstname