from django.db import models
from admin_panel.models import Products,partyDetails

# Create your models here.
class Invoice_Details(models.Model):
    party = models.ForeignKey(partyDetails, on_delete=models.DO_NOTHING)
    credit = models.IntegerField(null=False)
    debit = models.IntegerField(null=False)
    total = models.BigIntegerField(null=False)
    invoice_number = models.IntegerField(null=False)
    date_In = models.DateTimeField(null=False)
    class Meta:
        db_table = 'InvoiceDetails'


class Sales_Details(models.Model):
    pro= models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    salse_quantity = models.IntegerField(null=False)
    Invoice_id = models.ForeignKey(Invoice_Details,on_delete=models.DO_NOTHING)
    class Meta:
        db_table = 'SalseDetails'


