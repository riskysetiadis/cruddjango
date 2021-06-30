from .models import Emp
from django.shortcuts import render

def viewEmp(request, pk):
   emp = Emp.objects.get(id=pk)
   return render(request, 'view.html', {'emp': emp})
