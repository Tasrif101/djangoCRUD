from django.shortcuts import render, redirect
from .models import EmployeeDB
#from .models import VehiclesDB


def index(request):
    data=EmployeeDB.objects.all()
    context={"data":data}
    return render(request, "index.html",context)


def insertData(request):
    if request.method=="POST":
        name=request.POST.get('name')
        id=request.POST.get('id')
        status=request.POST.get('status')
        type=request.POST.get('type')
        gender=request.POST.get('gender')
        print(name,id,status,type,gender)
        query=EmployeeDB(name=name, id=id, status=status, type=type, gender=gender)
        query.save()
        return redirect("/")
    return render(request, "index.html")

# def insertData(request):
#     if request.method=="POST":
#         number=request.POST.get('number')
#         modelNumber=request.POST.get('modelNumber')
#         chasisNumber=request.POST.get('chasisNumber')
#         Mileage=request.POST.get('Mileage')
#         registrationNumber=request.POST.get('registrationNumber')
#         print(number,modelNumber,chasisNumber,Mileage,registrationNumber)
#         query=EmployeeDB(number=number, modelNumber=modelNumber, chasisNumber=chasisNumber, Mileage=Mileage, registrationNumber=registrationNumber)
#         query.save()
#     return render(request, "index.html")

def updateData(request,id):
    if request.method=="POST":
        name=request.POST.get('name')
        id=request.POST.get('id')
        status=request.POST.get('status')
        type=request.POST.get('type')
        gender=request.POST.get('gender')
        edit=EmployeeDB.objects.get(id=id)
        edit.name=name
        edit.id=id
        edit.status=status
        edit.type=type
        edit.gender=gender
        edit.save()
    d=EmployeeDB.objects.get(id=id)
    context={"d":d}
    return render(request, "edit.html",context)


def deleteData(request,id):
    d=EmployeeDB.objects.get(id=id)
    d.delete()
    return redirect("/")


# def insertData(request):
#     if request.method=="POST":
#         Number=request.POST.get('Number')
#         ModelNumber=request.POST.get('Model Number')
#         ChasisNumber=request.POST.get('Chasis Number')
#         Mileage=request.POST.get('Mileage')
#         RegistrationNumber=request.POST.get('Registration Number')
#         print(Number,ModelNumber,ChasisNumber,Mileage,RegistrationNumber)

#     return render(request, "index.html")


  
def about(request):
    return render(request, "about.html")
