from django.urls import path
from django.contrib import admin
from salles import views

urlpatterns = [
    path('invoice/', views.invoiceMaster, name='invoice_master'),
    path('invoice_add/', views.invoiceAdd, name='invoice_add'),
    path('sales_add/<int:id>', views.salesAdd, name='sales_add'),
    path('sales_details/<int:id>', views.salesDetails, name='sales_details'),
    path('generate-bills/',views.genrateBills,name='genrate')
]