from django.shortcuts import render
from .models import *

def home(request):
    project = Project.objects.all()
    context = {'project':project}
    return render(request, 'home.html', context)