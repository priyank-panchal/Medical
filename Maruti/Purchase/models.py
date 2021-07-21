from django.db import models
from admin_panel.models import Products,partyDetails
# Create your models here.

class Purchase_Details(models.Model):
    party = models.ForeignKey(partyDetails,on_delete=models.DO_NOTHING)
    Bill_no = models.IntegerField(null=False)
    date_pur = models.DateTimeField(null=False)
    class Meta:
        db_table = 'Purchase_details'

class Stock(models.Model):
    pro = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    salse_rate = models.IntegerField(null=False)
    purchase_rate = models.IntegerField(null=False)
    offer_rate = models.IntegerField(null=False)
    quantity = models.IntegerField(null=False)
    min_quantity = models.IntegerField(null=False)
    pur = models.ForeignKey(Purchase_Details,on_delete=models.DO_NOTHING)
    offer_qty = models.IntegerField(null=False)
    class Meta:
        db_table = 'Stock'
