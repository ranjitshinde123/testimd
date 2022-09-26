
from django.urls import path
from .views import *
urlpatterns = [

    path('supplier/',SupplierAPIView.as_view()),
    path('supplier/<int:pk>/',SupplierAPIView.as_view()),

    path('purchaseBill/',PurchaseBillAPIView.as_view()),
    path('purchaseBill/<int:pk>/',PurchaseBillAPIView.as_view()),

    path('purchaseitem/',PurchaseItemAPIView.as_view()),
    path('purchaseitem/<int:pk>/',PurchaseItemAPIView.as_view()),

    path('purchasebilldetail/',PurchaseBillDetailsAPIView.as_view()),
    path('purchasebilldetail/<int:pk>/',PurchaseBillDetailsAPIView.as_view()),

    path('salebill/',SaleBillAPIView.as_view()),
    path('salebill/<int:pk>/',SaleBillAPIView.as_view()),

    path('salebilldetails/',SaleBillDetailsAPIView.as_view()),
    path('salebilldetails/<int:pk>/',SaleBillDetailsAPIView.as_view()),
    path('saleitem/',SaleItemAPIView.as_view()),
    path('saleitem/<int:pk>/',SaleItemAPIView.as_view()),
]