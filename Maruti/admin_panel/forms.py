from django import forms
from .models import *

class Productform(forms.ModelForm):
    class Meta:
        model = Products
        fields =["pro_name","MRP"]

class Partyform(forms.ModelForm):
    class Meta:
        model = partyDetails
        fields = ["party_name","area","GST_No","party_type", "mobile_no"]

