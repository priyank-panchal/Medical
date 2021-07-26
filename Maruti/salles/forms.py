from django import forms
from admin_panel.models import *
from .models import *

class invoiceform(forms.ModelForm):
    class Meta:
        model = Invoice_Details
        fields = ["party","credit","debit","total","invoice_number","date_In"]

class sallesform(forms.ModelForm):
    class Meta:
        model = Sales_Details
        fields = ["pro","salse_quantity"]