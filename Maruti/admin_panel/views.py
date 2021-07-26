from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.db.models import Sum
from .models import Products
from .models import partyDetails
from Purchase.models import Purchase_Details
from .forms import *
from Purchase.models import Stock


# Create your views here.

def loginAdmin(request):
    if request.method == 'POST':
        uname = request.POST['username']
        passw = request.POST['password']
        user = auth.authenticate(username=uname, password=passw)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "succesfully login")
            return redirect("admin-home")
        else:
            messages.info(request, "User Name And password Does Not Match")
            return redirect("admin-login")
    else:
        return render(request, 'auth-login.html')


def index(request):
    return render(request, 'index.html')


def supplierDetail(request):
    allData = partyDetails.objects.all()
    context = {'party_list': allData}
    return render(request, "supplier-details.html", context)


def PartyAdd(request):
    if request.method == 'POST':
        allfield = Partyform(request.POST)
        if allfield.is_valid():
            allfield.save()
            messages.success(request, "succefull inserted")
            return redirect("party")
    else:
        allfield = Partyform()
    return render(request, "supplier-add.html")


def employeeDetail(request):
    return render(request, "employee_details.html")


def employeeAdd(request):
    return render(request, "employee_add.html")


def productDetails(request):
    allproduct = Products.objects.all()
    allData = Products.objects.values_list('pro_id', flat=True)
    values = []
    for i in range(0, len(allData)):
        values.append(Stock.objects.filter(pro_id=allData[i]).aggregate(Sum('quantity')))
    zipped_final_products = zip(allproduct, values)
    allDataIndex = {
        'product_list': zipped_final_products
    }
    return render(request, "product_details.html", allDataIndex)


def productAdd(request):
    if request.method == 'POST':
        allFields = Productform(request.POST)
        if allFields.is_valid():
            allFields.save()
            messages.success(request, "succesfully inserted")
            return redirect('product_details')
    else:
        allFields = Productform()
    return render(request, "product_add.html")


def productDelete(request,pro_id):
    deleteproduct = Products.objects.get(pro_id=pro_id)
    deleteproduct.delete()
    messages.success(request,"Successfully deleted")
    return redirect('product_details')

def demoPur(request):
    return render(request,"demopage.html")
