from django.shortcuts import render
from django.http import HttpResponse
from census import censusDataUtils
from census.models import InfoType
from census.models import CensusInfo
from .models import Greeting
import os

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

def add_zip(request):
  zips = request.POST.getlist("zipcode")
  statecode = request.POST.getlist("statecode")
  state = statecode[0]
  retStr = ""
  for zip in zips:
    retStr += populateDataForZip(zip) + "\n\n ---- "
  return HttpResponse("Success: " + retStr

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def populateDataForZip(zip):
    apiKey = os.environ['CENSUS_API_KEY']
    infoTypes = InfoType.objects.all()
    data = censusDataUtils.fetchAndFormCensusInfoForZip(zip, 6, apiKey, infoTypes)
    retStr = ""
    for d in data:
      retStr += d.info + ": "
      d.save()
    return retStr
