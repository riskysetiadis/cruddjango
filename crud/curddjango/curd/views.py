from django.shortcuts import render, HttpResponse, redirect
from .models import Emp
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def createView(request):
    return render(request, 'create.html')

@csrf_exempt
def store(request):
    emp = Emp()
    emp.emp_name = request.POST.get('emp_name')
    emp.emp_email = request.POST.get('emp_email')
    emp.emp_mobile = request.POST.get('emp_mobile')
    emp.save()
    messages.success(request, "Employee Added Successfully")
    return redirect('/create')

@csrf_exempt
def index(request):
    emp = Emp.objects.all()
    return render(request, 'index.html', {'emp': emp})


@csrf_exempt
def viewEmp(request, pk):
   emp = Emp.objects.get(id=pk)
   return render(request, 'view.html', {'emp': emp})


@csrf_exempt
def deleteEmp(request, pk):
    emp = Emp.objects.get(id = pk)
    emp.delete()
    messages.success(request, "Employee Deleted Successfully")
    return redirect('/')


@csrf_exempt
def updateView(request,pk):
    emp = Emp.objects.get(id = pk)
    return render(request,'update.html',{'emp':emp})


@csrf_exempt
def update(request, pk):
    print('in')
    emp = Emp.objects.get(id=pk)
    emp.emp_name = request.POST.get('emp_name')
    emp.emp_email = request.POST.get('emp_email')
    emp.emp_mobile = request.POST.get('emp_mobile')
    emp.save()
    messages.success(request, "Employee Update Successfully")
    return redirect('/')
