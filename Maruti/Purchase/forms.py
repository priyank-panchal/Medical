from django import forms
from admin_panel.models import *
from .models import *
class Purchaseform(forms.ModelForm):
    class Meta:
        model = Purchase_Details
        fields =["party","Bill_no","date_pur"]

class Stockform(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["salse_rate","purchase_rate","offer_rate","quantity","min_quantity","offer_qty","pro"]