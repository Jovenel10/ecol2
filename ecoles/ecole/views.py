from django.shortcuts import render
from django.http import HttpResponse
from ecole.models import ecole

# Create your views here.
def affichage(request):
    ecoles=ecole.objects.all()
    #return HttpResponse(ecole)

  # return render(request, 'index.html',{'ecole':ecole})
