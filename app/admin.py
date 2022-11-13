from django.contrib import admin
from django.utils.html import format_html

from .models import Candidate
from .forms import CandidateForm

# Register your models here.

class CandidateAdmin(admin.ModelAdmin):
    radio_fields = {'smoker': admin.HORIZONTAL}
    form = CandidateForm
    readonly_fields = ['email', 'job', 'age', 'phone']
    exclude = ['status']
    list_filter = ['Situation']
    list_display = ['name', 'email', 'job', 'age', 'created', 'status', '_']
    search_fields = ['firstname', 'lastname', 'email', 'age', 'Situation']
    list_per_page = 25

    # Function to hide F-name and L-name (When clicking over the candidates -- Rows)
    def get_fields(self, request, obj = None):
        fields = super().get_fields(request, obj)
        if obj :
            fields.remove('firstname')
            fields.remove('lastname')
        return fields

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

