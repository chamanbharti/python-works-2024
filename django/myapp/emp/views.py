from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def emp_home(request):
    #return HttpResponse("student home page")
    return render(request, "emp/home.html")
