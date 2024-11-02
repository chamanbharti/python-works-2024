import datetime
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    #print("test function is called from view")
    #return HttpResponse("<h1>Hello This is index page</h1>")
    isActive = None
    if request.method == 'POST':
        check = request.POST['check']
        #check = request.POST.get('check')
        print("check:"+check)
        if check is None: isActive=False
        else: isActive=True
    
    date = datetime.datetime.now()
    
    name = "Chaman Bharti"
    list_of_programs = ["WAP to check even or odd",
                        "WAP to check prime number",
                        "WAP to print all prime numbers form 1 to 100",
                        "WAP to print pascals triangle"
                        ]
    students = {
        'student_name':"Chaman",
        'student_college':"IGNOU",
        'student_city':"Noida"
    }
    data = {
        'date':date,
        'isActive':isActive,
        'name': name,
        'list_of_programs':list_of_programs,
        'student_data':students
    }
    return render(request,"home.html",data)

def about(request):
    #return HttpResponse("<h1>Hello This is about page</h1>")
    return render(request,"about.html",{})

def services(request):
    #return HttpResponse("<h1>This is services page</h1>")
    return render(request,"services.html",{})