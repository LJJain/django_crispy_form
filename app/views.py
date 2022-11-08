from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect

from .forms import CandidateForm

# Create your views here.

def home(request):
    forms=CandidateForm
    if request.method == 'POST':
        forms= CandidateForm(request.POST or None)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Register is successful')
            return HttpResponseRedirect('/')

    context = {'forms': forms}
    return render(request, 'home.html', context)