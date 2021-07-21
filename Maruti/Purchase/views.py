from django.shortcuts import render
from Purchase.models import Purchase_Details
from admin_panel.models import partyDetails,Products
# Create your views here.
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
def stockMaster(request):
    return render(request,"stock_master.html")

def stockAdd(request,Pur_id):
    if request.method == 'POST':
        allfield = Stockform(request.POST or None)
        if allfield.is_valid():
            confirm = allfield.save(commit=False)
            confirm.pur = Purchase_Details.objects.get(Pur_id=Pur_id)
            confirm.save()
            return redirect('party')
    allData =Products.objects.all()
    context ={
        "all_product":allData
    }
    return render(request,"stock_add.html",context)
