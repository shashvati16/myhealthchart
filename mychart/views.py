from django.shortcuts import render
from django.http import HttpResponse

userdb = {"Name": "Shashvati Dash", "DOB": "05/19/1987", "Gender": "F", "Bloodgroup":"O+", "Covidtest":"-ve"}
def index(request):
    text=""
    for x in userdb:
      text = text + "\n" + x + ": " + userdb[x]
     
    return HttpResponse(text)