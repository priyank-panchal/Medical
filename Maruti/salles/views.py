from django.shortcuts import render

def invoiceMaster(request):
    return render(request,"invoice_master.html")

def invoiceAdd(request):
    return render(request,"invoice_add.html")

def salesAdd(request):
    return render(request,"sales_add.html")

def salesDetails(request):
    return render(request,"sales_details.html")
