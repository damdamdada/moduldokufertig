from django.shortcuts import render
from .models import Hack
# Create your views here.
def hacken(request):
    hacks = Hack.objects.all()
    return render(request, 'hacken/hacken.html',{'hacks':hacks})
