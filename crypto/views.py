from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    number=[1,2,3,4,5]
    name = 'yogesh'

    args={'myName': name, 'numbers':number}        
       
    return render(request, 'crypto/home.html', args)