from django.contrib import admin

from .models import Candidate

# Register your models here.

class CandidateAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email', 'job', 'age', 'created']
    search_fields = ['firstname', 'lastname', 'email', 'age']
    list_per_page = 25

    # function to change the icons
    def _(self, obj):
        if obj.situation == 'Approved':
            return True
        elif obj.situation == 'Pending':
            return None
        else:
            return False
    _.boolean = True

    # function to color the text
        

admin.site.register(Candidate, CandidateAdmin)

