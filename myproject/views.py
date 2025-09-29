from django.shortcuts import render, redirect
from myapp.models import employeeModel, designationModel

def basepage(request):
    return render(request, 'base.html')

def empformpage(request):
    designations = designationModel.objects.all()

    if request.method == 'POST':
        emp_name = request.POST.get('emp_name')
        emp_id = (request.POST.get('emp_id'))
        emp_city = request.POST.get('emp_city')
        emp_salary = float(request.POST.get('emp_salary'))
        emp_DOB = request.POST.get('emp_DOB')
        emp_email = request.POST.get('emp_email')
        emp_phone = request.POST.get('emp_phone')
        emp_address = request.POST.get('emp_address')
        emp_photo = request.FILES.get('emp_photo')
        designation_id = request.POST.get('designation_id')
        overtime_hours = float(request.POST.get('overtime'))
        date_of_joining = request.POST.get('date_of_joining')
        bonus = float(request.POST.get('bonus'))

        # Fetch designation object
        designation = designationModel.objects.get(id=designation_id)

        # Salary components (these can be made dynamic later)
        HRA_percent = 0
        DA_percent = 0
        TA_percent = 0

        HRA = (HRA_percent * emp_salary) / 100
        DA = (DA_percent * emp_salary) / 100
        TA = (TA_percent * emp_salary) / 100
        overtime_amount = overtime_hours * 100

        gross_salary = emp_salary + HRA + DA + TA + overtime_amount + bonus

        emp = employeeModel(
            emp_name=emp_name,
            emp_id=emp_id,
            emp_city=emp_city,
            basic_salary=emp_salary,
            emp_DOB=emp_DOB,
            emp_email=emp_email,
            emp_phone=emp_phone,
            emp_address=emp_address,
            emp_photo=emp_photo,
            bonus=bonus,
            overtime=overtime_hours,
            salary=gross_salary,
            date_of_joining=date_of_joining,
            designation=designation
        )
        emp.save()
        return redirect('empdata')

    context = {'designations': designations}
    return render(request, 'empform.html', context)

def empdatapage(request):
    data = employeeModel.objects.all()
    return render(request, 'empdata.html', {'employees': data})

def aboutpage(request):
    return render(request, 'about.html')
