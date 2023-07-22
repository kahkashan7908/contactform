from django.shortcuts import render
from .models import empData
def mainPage(request): 
    if request.method=='GET':
        return render(request,'contactform.html')
    else:
        empData(
            first_name=request.POST['Fname'],
            last_name=request.POST['Lname'],
            email=request.POST['email'],
            mobile=request.POST['mobile'],
            location=request.POST['location']
        ).save(),
        return render(request,'contactform.html')
    
