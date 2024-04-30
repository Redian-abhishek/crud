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
    employees = Employee.objects.all()

    paginator = Paginator(employees, 10)  # Set 1 employee per page
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


def search(request):
    query = request.GET.get('q')
    employees = Employee.objects.all()  

    if query:
        employees = employees.filter(                        
            Q(id__icontains=query) |
            Q(eid__icontains=query) |
            Q(ename__icontains=query) |
            Q(eemail__icontains=query) |
            Q(econtact__icontains=query)
        )

    paginator = Paginator(employees, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if not page_obj:
        print("Not found")

    return render(request, "search.html", {'page_obj': page_obj})