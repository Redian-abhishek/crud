from django.shortcuts import render, redirect
from employee.forms import EmployeeForm
from employee.models import Employee
from django.core.paginator import Paginator
from django.db.models import Q


def landing_page(request):
    return render(request, 'landing_page.html')

def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/show')
    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form': form})

def show(request):
    query = request.GET.get('q')
    if query:
        employees = Employee.objects.filter(
            Q(eid__icontains=query) |
            Q(ename__icontains=query) |
            Q(eemail__icontains=query) |
            Q(econtact__icontains=query)
        )
    if not employees:
            print("Not found")

    paginator = Paginator(employees, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "show.html", {'page_obj': page_obj})

 

def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})

def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})

def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")


