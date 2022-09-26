
from django.urls import path

from .views import StockAPIView,Register

urlpatterns = [
    # for otp
    # path('send-otp/', send_otp),
    # path('verify-otp',verify_otp),

    # for stock
    path('',Register.as_view()),
    path('stock/',StockAPIView.as_view()),
    path('stock/<int:pk>/',StockAPIView.as_view()),
]