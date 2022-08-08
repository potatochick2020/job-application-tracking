from django.shortcuts import render
import pymongo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Userjob
from .serializers import UserjobSerializer

client = pymongo.MongoClient("mongodb+srv://dev:12341234@cluster0.y71di.mongodb.net/?retryWrites=true&w=majority")
db = client.gettingStarted
userjob_collection = db.userjob_collection
# Create your views here.


  
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
  
    return Response(api_urls)

from rest_framework import serializers
from rest_framework import status

sample_data = {
    "email" : "admspamdaskd.com",
    "jobId" : "dksalkdasdokasd"
}

print(sample_data)

@api_view(['POST'])
def add_items(request):
    print(sample_data)
    #userjob_collection.insert_one(sample_data)
    return Response(sample_data)