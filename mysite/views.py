from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from mysite.models import *



def index(request):
    return render(request,'mysite/index.html')


def addDepartment(request):
    m1=""
    Title = "New"
    if request.method == 'POST':
        num = request.session.get('Dept')
        if "0" is not num:
            Department.objects.filter(Departnemt_Name__iexact=num).delete()
            Title = "Edit"
        DeptName = request.POST.get("desname")
        hr = request.POST.get("select")
        filterr = Department.objects.filter(Departnemt_Name__iexact=DeptName).first()
        if filterr is None:
            c = Department(Departnemt_Name=DeptName, HRManager=hr)
            c.save()
            m1 = "Data Saved Sucessfully"
        else:
            m1 = "Data Already Exists"
            request.session['Dept'] = "0"

    context = {
        'posts':HRManager.objects.all(),
        'messagess': m1,
        'title': Title
    }

    return render(request,'mysite/departments/adddept.html',context)




def ViewDepartment(request):
    context = {
        'posts': Department.objects.all()
    }

    return render(request,'mysite/departments/viewdept.html',context)




def DeleteDepartment(request):
    m1 = ""
    m2 = ""
    title = "Edit"
    if request.method == 'POST':
        abc = request.POST.get("select")
        if abc is not None and 'Edit' in request.POST :                     #edit button pressed
            request.session['Dept'] = abc
            context = {
                    'title':title,
                    'dname':abc,
                    'messagess':"",
                    'posts':HRManager.objects.all(),
            }
            return render(request, 'mysite/departments/adddept.html', context)
        if abc is not None and 'Delete' in request.POST:  # delete Button Pressed
            Department.objects.filter(Departnemt_Name__iexact=abc).delete()
            m1 = "Data Deleted Sucessfully"
            filterr = Department.objects.first()
            if filterr is not None:
                m2 = "return confirm('Are you sure you want to delete this item?');"
            else:
                m2 = ""
        else:
            m1 = "Data Not Exists"
    else:
        filterr = Department.objects.first()
        if filterr is not None:
            m2 = "return confirm('Are you sure you want to delete this item?');"
        else:
            m2 = ""
        m1 = ""
    context = {
        'posts': Department.objects.all(),
        'messagess': m1,
        'm': m2
    }
    return render(request,'mysite/departments/deldept.html',context)



#------------------------------------------------------------------------------------------------------------

def addDesignation(request):
    m1=""
    Title="New"
    if request.method == 'POST':
        num = request.session.get('Des')
        if "0" is not num:
            Designation.objects.filter(DesignationName__iexact=num).delete()
            Title = "Edit"
        DesName = request.POST.get("desname")
        status=request.POST.get("Select")
        filterr=Designation.objects.filter(DesignationName__iexact=DesName).first()
        if filterr is None:
            c=Designation(DesignationName=DesName,Status=status)
            c.save()
            m1="Data Saved Sucessfully"
        else:
            m1="Data Already Exists"
            request.session['Des'] = "0"

    context = {
        'messagess': m1,
        'title':Title
    }
    return render(request, 'mysite/designations/add.html',context)



def ViewDesignation(request):
    context={
        'posts':Designation.objects.all()
    }
    return render(request,'mysite/designations/view.html',context)


def RemoveDesignation(request):
    m1=""
    m2 = ""
    title="Edit"
    if request.method == 'POST':
        abc = request.POST.get("select")
        if abc is not None and 'Edit' in request.POST :                     #edit button pressed
            request.session['Des'] = abc
            context = {
                    'title':title,
                    'dname':abc,
                    'messagess':"",
            }
            return render(request, 'mysite/designations/add.html', context)
        if abc is not None and 'Delete' in request.POST :                                    #delete Button Pressed
            Designation.objects.filter(DesignationName__iexact=abc).delete()
            m1="Data Deleted Sucessfully"
            filterr = Designation.objects.first()
            if filterr is not None:
                m2 = "return confirm('Are you sure you want to delete this item?');"
            else:
                m2 = ""

        else:
            m1="Data Not Exists"
    else:
        filterr = Designation.objects.first()
        if filterr is not None:
            m2 = "return confirm('Are you sure you want to delete this item?');"
        else:
            m2 = ""
        m1=""
    context = {
        'posts': Designation.objects.all(),
        'messagess':m1,
        'm':m2
    }
    return render(request, 'mysite/designations/delete.html', context)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def addOffice(request):
    m1 = ""
    Title = "New"
    if request.method == 'POST':
        num = request.session.get('ofc')
        if "0" is not num:
            Offices.objects.filter(Offices_Name__iexact=num).delete()
            Title = "Edit"

        officeName = request.POST.get("desname")
        hr = request.POST.get("select")
        filterr = Offices.objects.filter(Offices_Name__iexact=officeName).first()
        if filterr is None:
            c = Offices(Offices_Name=officeName, HRManager=hr)
            c.save()
            m1 = "Data Saved Sucessfully"
            request.session['ofc'] = "0"
        else:
            m1 = "Data Already Exists"
            request.session['ofc'] = "0"

    context = {
        'posts': HRManager.objects.all(),
        'messagess': m1,
        'title': Title
    }
    return render(request,'mysite/offices/addoffice.html',context)

def viewOffice(request):
    context = {
        'posts': Offices.objects.all()
    }

    return render(request,'mysite/offices/viewoffices.html',context)

def RemoveOffice(request):
    m1 = ""
    m2 = ""
    title = "Edit"
    if request.method == 'POST':
        abc = request.POST.get("select")
        if abc is not None and 'Edit' in request.POST:  # edit button pressed
            request.session['ofc'] = abc
            context = {
                'title': title,
                'dname': abc,
                'messagess': "",
                'posts': HRManager.objects.all(),
            }
            return render(request, 'mysite/offices/addoffice.html', context)

        if abc is not None and 'Delete' in request.POST:  # delete Button Pressed
            Offices.objects.filter(Offices_Name__iexact=abc).delete()
            m1 = "Data Deleted Sucessfully"
            filterr = Offices.objects.first()
            if filterr is not None:
                m2 = "return confirm('Are you sure you want to delete this item?');"
            else:
                m2 = ""
        else:
            m1 = "Data Not Exists"
    else:
        filterr = Offices.objects.first()
        if filterr is not None:
            m2 = "return confirm('Are you sure you want to delete this item?');"
        else:
            m2 = ""
        m1 = ""
    context = {
        'posts': Offices.objects.all(),
        'messagess': m1,
        'm': m2
    }
    return render(request,'mysite/offices/deleteoffice.html',context)


