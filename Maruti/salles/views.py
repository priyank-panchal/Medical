from django.shortcuts import render,redirect
from admin_panel.models import Products,partyDetails
from salles.forms import invoiceform,sallesform
from Purchase.models import Stock
from Purchase.models import Purchase_Details
from django.contrib import messages
from .models import Invoice_Details,Sales_Details
from django.db.models import Sum
import sys
def genrateBills(request):
    return render(request,"invoice-generate.html")
def invoiceMaster(request):
    allData = Invoice_Details.objects.all()
    context = {
        "all_invoice":allData
    }
    return render(request,"invoice_master.html",context)

def invoiceAdd(request):
    if request.method == "POST":
        allfield = invoiceform(request.POST or None)
        if allfield.is_valid():
            allfield.save()
            messages.success(request, "successfully added")
            return redirect('invoice_master')
    allData = partyDetails.objects.all()
    context = {
            "all_party": allData
    }
    return render(request,"invoice_add.html",context)

def salesAdd(request,id):
    if request.method == 'POST':
        allfield = sallesform(request.POST or None)
        if allfield.is_valid():
            sales_qty = allfield.cleaned_data['salse_quantity']
            product_id =allfield.cleaned_data['pro']
            isValid = False
            try:
               total_qty = Stock.objects.filter(pro_id=product_id).aggregate(Sum('quantity'))
               if total_qty['quantity__sum'] >= sales_qty:
                    update_qty = Stock.objects.filter(pro = product_id)[0]
                    if update_qty.quantity > sales_qty:
                        update_qty.quantity = update_qty.quantity - sales_qty
                        isValid = True
                        update_qty.save()
                    else:
                        sales_qty = sales_qty - update_qty.quantity
                        update_qty.delete()
                        while True:
                             update_qty = Stock.objects.filter(pro = product_id)[0]
                             if update_qty.quantity >= sales_qty:
                                update_qty.quantity = update_qty.quantity - sales_qty
                                update_qty.save()
                                break
                             else:
                                sales_qty = sales_qty - update_qty.quantity
                                update_qty.delete()
               else:
                 messages.error(request, "Not have enough quantity")
            except ObjectDoesNotExist:
                return HttpResponse("Exception: Data not found")
            if isValid:
               confirm = allfield.save(commit=False)
               confirm.Invoice_id = Invoice_Details.objects.get(id = id)
               confirm.save()
               print("jay meldi ma")
               return redirect('invoice_master')

    allData =Products.objects.all()
    context ={
        "all_product":allData
    }
    return render(request,"sales_add.html",context)

def salesDetails(request):
    return render(request,"sales_details.html")
