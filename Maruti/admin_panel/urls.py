from django.urls import path
from django.contrib import admin
from admin_panel import views
urlpatterns = [
    path('login/', views.loginAdmin, name='admin-login'),
    path('index/', views.index, name='admin-home'),
    path('party/', views.supplierDetail, name='party'),
    path('Party-add/', views.PartyAdd, name='supplier-add'),
    path('employee/', views.employeeDetail, name='employee-details'),
    path('employee_add/', views.employeeAdd, name='employee_add'),
    path('product_details/', views.productDetails, name='product_details'),
    path('product_add/', views.productAdd, name='product_add'),
    path('demo/',views.demoPur,name='purpose'),
    path('product_delete/<int:pro_id>/',views.productDelete,name='product_delete'),
]