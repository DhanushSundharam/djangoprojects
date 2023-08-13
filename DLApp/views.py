from django.shortcuts import render
from DLApp.models import Employee

def input_view(request):
    input_value = None
    input_value2=None
    
    
    if request.method == 'POST':
        input_value = request.POST.get('username_or_email', None)
        input_value2 = request.POST.get('password', None)
        emp_data=Employee.objects.create(empNo=input_value,empName=input_value2)
    
    context = {'input_value': input_value,'input_value2':input_value2}
    return render(request, 'DLApp/index.html', context)
