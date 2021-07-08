from django.http import HttpResponse
from django.shortcuts import render
from .models import Athlete, Family

# Create your views here.
# def home_view(*args, **kwargs):
#     return HttpResponse("first")

def home_view(request, *args, **kwargs):
    families = Family.objects.all()
    # my_context={
    #     "my_text": "Az is the best there is!"
    # } 
    return render(request, "home.html", {'families' : families})
