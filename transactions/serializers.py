


from rest_framework import serializers
from .models import*


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model=Supplier
        fields='__all__'



class PurchaseBillSerializer(serializers.ModelSerializer):
    class Meta:
        model=PurchaseBill
        fields='__all__'


class PurchaseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=PurchaseItem
        fields='__all__'


class PurchaseBillDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=PurchaseBillDetails
        fields='__all__'


class SaleBillSerializer(serializers.ModelSerializer):
    class Meta:
        model=SaleBill
        fields='__all__'


class SaleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=SaleItem
        fields='__all__'


class SaleBillDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=SaleBillDetails
        fields='__all__'