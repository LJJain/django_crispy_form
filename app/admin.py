from django.contrib import admin
from django.utils.html import format_html

from .models import Candidate
from .forms import CandidateForm

# Register your models here.

class CandidateAdmin(admin.ModelAdmin):
    radio_fields = {'smoker': admin.HORIZONTAL}
    form = CandidateForm
    list_filter = ['Situation']
    list_display = ['firstname', 'lastname', 'email', 'job', 'age', 'created', 'status', '_']
    search_fields = ['firstname', 'lastname', 'email', 'age', 'Situation']
    list_per_page = 25

    # function to change the icons
    def _(self, obj):
        if obj.Situation == 'Approved':
            return True
        elif obj.Situation == 'Pending':
            return None
        else:
            return False
    _.boolean = True

    # function to color the text
    def status(self, obj):
        if obj.Situation == 'Approved':
            color = '#28a745'
        elif  obj.Situation == 'Pending':
            color = '#fea95e'
        else:
            color = 'red'
        return format_html('<strong><p style="color:{}">{}</p></strong'.format(color, obj.Situation))
    status.allow_tags = True
        

admin.site.register(Candidate, CandidateAdmin)

