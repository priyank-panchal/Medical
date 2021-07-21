from django.db import models

class Products(models.Model):
    pro_id = models.AutoField(primary_key=True)
    pro_name = models.CharField(max_length=50,null=False)
    MRP = models.IntegerField(null=False)
    class Meta:
        db_table = 'Products_details'

class partyDetails(models.Model):
    party_id  = models.AutoField(primary_key=True)
    party_name = models.CharField(max_length=40)
    area = models.CharField(max_length=40,blank=True,null=True)
    GST_No = models.CharField(max_length=50, blank=True, null=True)
    party_type = models.CharField(max_length=15)
    mobile_no = models.IntegerField()
    class Meta:
        db_table = 'Party_details'

