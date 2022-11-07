from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect

from .forms import CandidatesForm

# Create your views here.

def home(request):
    forms=CandidatesForm
    if request.method == 'POST':
        forms= CandidatesForm(request.POST or None)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Register is successful')
            return HttpResponseRedirect('/')

    context = {'forms': forms}
    return render(request, 'home.html', context)