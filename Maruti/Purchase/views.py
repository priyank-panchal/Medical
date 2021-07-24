from django.shortcuts import render,redirect
from .models import Purchase_Details,Stock
from django.urls import reverse
from admin_panel.models import partyDetails,Products
from Purchase.forms import Purchaseform,Stockform
from django.contrib import messages


def purchaseDetail(request):
    allData = Purchase_Details.objects.all()
    context = {
        "all_purchase":allData
    }
    return render(request,"purchase-details.html",context)

def purchaseAdd(request):
        if request.method == "POST":
           allfield = Purchaseform(request.POST or None)
           if allfield.is_valid():
               allfield.save()
               messages.success(request,"successfully added")
               return redirect("purchase-details")
        allData = partyDetails.objects.all()
        context = {
            "all_party":allData
        }
        return render(request,"purchase-add.html",context)
def stockMaster(request,id):
    ShowStock = Stock.objects.filter(pur=id)
    context = {
        "stock_details":ShowStock
    }
    return render(request,"stock_master.html",context)

def stockAdd(request,id):
    if request.method == 'POST':
        allfield = Stockform(request.POST or None)
        if allfield.is_valid():
            confirm = allfield.save(commit=False)
            confirm.pur = Purchase_Details.objects.get(id=id)
            confirm.save()
            return redirect('purchase-details')
    allData =Products.objects.all()
    context ={
        "all_product":allData
    }
    return render(request,"stock_add.html",context)