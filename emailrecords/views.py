from django.shortcuts import render
from django.http import HttpResponse
from .models import emailrecords

# Create your views here.
def index(request):

    emailrecord = emailrecords.objects.all()[:10]

    context = {
        'name': 'Email holders',
        'email': emailrecord
    }


    return render(request, 'pages/index.html', context)

def list(request):
    return render(request, 'emailrecords/list.html')
