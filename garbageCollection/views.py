from django.shortcuts import render
import requests
from django.http import HttpResponse
from garbageCollection.models import CollectionDetails
import json
# Create your views here.

# All the legal borough  
legal_borough = ['Brooklyn', 'Manhattan', 'Bronx', 'Queens', 'Statenisland']
# All the legal Community District IDs
legal_communitydistrict = ['01', '02', '03', '04', '05', '06', '07',
                           '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18']

# API endpoint number 1


def refuse(request):
    borough = request.GET['borough']
    communitydistrict = request.GET['communitydistrict']
    borough = borough[0].upper()+borough[1:].lower()
    responses = SendRequests(borough, communitydistrict, request.GET['month']) if 'month' in request.GET.keys() else SendRequests(
        borough, communitydistrict)
    refusetonscollected = 0
    for response in responses.json():
        refusetonscollected += float(response['refusetonscollected'])
        print(response['refusetonscollected'])
    return SaveData(borough, communitydistrict, 'refuse', refusetonscollected)

# API endpoint number 2


def paper(request):
    borough = request.GET['borough']
    communitydistrict = request.GET['communitydistrict']
    borough = borough[0].upper()+borough[1:].lower()
    responses = SendRequests(borough, communitydistrict, request.GET['month']) if 'month' in request.GET.keys() else SendRequests(
        borough, communitydistrict)
    paper_collected = 0
    for response in responses.json():
        paper_collected += float(response['papertonscollected'])
        print(response['papertonscollected'])
    return SaveData(borough, communitydistrict, 'paper', paper_collected)

# API endpoint number 3


def mgp(request):
    borough = request.GET['borough']
    communitydistrict = request.GET['communitydistrict']
    borough = borough[0].upper()+borough[1:].lower()
    responses = SendRequests(borough, communitydistrict, request.GET['month']) if 'month' in request.GET.keys() else SendRequests(
        borough, communitydistrict)
    mgp = 0
    for response in responses.json():
        mgp += float(response['mgptonscollected'])
        print(response['mgptonscollected'])
    return SaveData(borough, communitydistrict, 'mgp', mgp)

# API endpoint number 4


def total(request):
    all_data = CollectionDetails.objects.all()
    print(all_data)
    total = 0.0
    for data in all_data:
        total += data.values
    return HttpResponse(total)

# Landing page with instructions and API end point descriptions


def hello(request):
    return HttpResponse("<h3>Please follow the url patterns</h3><br>")

# To hit the api with a get request


def SendRequests(borough, communitydistrict, month='2015 / 01'):
    url = f'https://data.cityofnewyork.us/resource/ebb7-mvp5.json?borough={borough}&communitydistrict={communitydistrict}&month={month}'
    return requests.get(url)

# To save the data into the database and return the response.


def SaveData(borough, communitydistrict, type, value):
    print(borough, communitydistrict, type, value)
    if borough in legal_borough and communitydistrict in legal_communitydistrict:
        collection_details_obj = CollectionDetails(
            types=type, borough=borough, community_district=communitydistrict, values=float(value))
        collection_details_obj.save()
        return HttpResponse(value)
    return HttpResponse(0)
