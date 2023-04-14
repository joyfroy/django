


import csv

from django.shortcuts import redirect, render


# Create your views here.


import csv


def index(request):

    return render(request, 'index.html')

def add(request):

    val1=request.GET['num1']
    val2=request.GET['num2']
    res=val1+val2




    return render(request,'result.html',{'result':res})

def search(request):
    with open('static/assets/final.csv', 'r') as csvfile:
        # read the csv file into a dictionary
        reader = csv.DictReader(csvfile)
        # get user input for disease name
        disease = request.GET['num1']
        # search for drug name corresponding to the disease name
        for row in reader:
            if row['Disease'] == disease:

                return render(request,'result.html', {'result':row['Drug']} )
                break
        else:
            return render(request,'result.html',{'result':'No drugs found'})

