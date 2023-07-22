from django.shortcuts import render,redirect
from .models import studentData
def mainPage(request):
    data= studentData.objects.all()
    return render(request,'mainpage.html',{'data':data})
def studentPage(request):
    if request.method=='GET':
        return render(request,'studentData.html')
    else:
        studentData(
            first_name=request.POST['fname'],
            last_name=request.POST['lname'],
            emil=request.POST['email'],
            mobile=request.POST['mobile'],
            iname=request.POST['iname'],
            fee=request.POST['fee'],
            marks=request.POST['marks'],
            location=request.POST['location']
        ).save()
        return redirect('mainPage')
    
def updatePage(request,id):
    data=studentData.objects.get(id=id)
    if request.method=='GET':
        return render(request,'update.html',{'val':data})
    else:
        data.first_name=request.POST['fname']
        data.last_name=request.POST['lname']
        data.emil=request.POST['email']
        data.mobile=request.POST['mobile']
        data.iname=request.POST['iname']
        data.fee=request.POST['fee']
        data.marks=request.POST['marks']
        data.location=request.POST['location']
        data.save()
        return redirect('mainPage')
    
def deleteData(request,id):
    data=studentData.objects.get(id=id)
    data.delete()
    return redirect('mainPage')



