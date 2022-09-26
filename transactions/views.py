from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import *



# Supplier class
class SupplierAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_fields = ['name']

    def get_object(self, pk):
        try:
            return Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            raise

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = SupplierSerializer(data)
            return Response(serializer.data)
        else:
            data = Supplier.objects.all()
            serializer = SupplierSerializer(data, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = SupplierSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            'message': 'Supplier Add Successfully',
            'data': serializer.data
        }
        return response

    def put(self, request, pk=None, format=None):
        Supplier_to_update = Supplier.objects.get(pk=pk)
        serializer = SupplierSerializer(instance=Supplier_to_update, data=request.data, partial=True)

        serializer.is_valid()
        serializer.save()
        response = Response()
        response.data = {
            'message': 'Supplier Updated Successfully',
            'data': serializer.data
        }
        return response

    def delete(self, request, pk, format=None):
        Stock_to_delete = Supplier.objects.get(pk=pk)
        Stock_to_delete.delete()
        return Response({
            'message': 'Suppllier deleted successfully'
        })

# PurchaseBill

class PurchaseBillAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    # filter_fields = ['name', 'category', 'subcategory', 'type']

    def get_object(self, pk):
        try:
            return PurchaseBill.objects.get(pk=pk)
        except PurchaseBill.DoesNotExist:
            raise
    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = PurchaseBillSerializer(data)
            return Response(serializer.data)
        else:
            data = PurchaseBill.objects.all()
            serializer = PurchaseBillSerializer(data, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = PurchaseBillSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            'message': 'Purchase Successfully',
            'data': serializer.data
            }
        return response

    def put(self, request, pk=None, format=None):
        Purchase_to_update = PurchaseBill.objects.get(pk=pk)
        serializer = PurchaseBillSerializer(instance=Purchase_to_update, data=request.data, partial=True)
        serializer.is_valid()
        serializer.save()
        response = Response()
        response.data = {
            'message': 'PurchaseBill Updated Successfully',
            'data': serializer.data
            }
        return response

    def delete(self, request, pk, format=None):
        Purchase_to_delete = PurchaseBill.objects.get(pk=pk)
        Purchase_to_delete.delete()
        return Response({
            'message': 'PurchaseBill deleted successfully'
        })

# PurchaseItem
class PurchaseItemAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def get_object(self, pk):
        try:
            return PurchaseItem.objects.get(pk=pk)
        except PurchaseItem.DoesNotExist:
            raise

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = PurchaseItemSerializer(data)
            return Response(serializer.data)
        else:
            data = PurchaseItem.objects.all()
            serializer = PurchaseItemSerializer(data, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = PurchaseItemSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            'message': 'PurchaseItem Add Successfully',
            'data': serializer.data
        }
        return response

    def put(self, request, pk=None, format=None):
        PurchaseItem_to_update = PurchaseItem.objects.get(pk=pk)
        serializer = PurchaseItemSerializer(instance=PurchaseItem_to_update, data=request.data, partial=True)
        serializer.is_valid()
        serializer.save()
        response = Response()
        response.data = {
            'message': 'PurchaseItem Updated Successfully',
            'data': serializer.data
        }
        return response

    def delete(self, request, pk, format=None):
        Purchase_to_delete = PurchaseItem.objects.get(pk=pk)
        Purchase_to_delete.delete()
        return Response({
            'message': 'PurchaseItem deleted successfully'
        })
# PurchaseBill
class PurchaseBillDetailsAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def get_object(self, pk):
        try:
            return PurchaseBillDetails.objects.get(pk=pk)
        except PurchaseBillDetails.DoesNotExist:
            raise

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = PurchaseBillDetailsSerializer(data)
            return Response(serializer.data)
        else:
            data = PurchaseBillDetails.objects.all()
            serializer = PurchaseBillDetailsSerializer(data, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = PurchaseBillDetailsSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            'message': 'Purchase details Add Successfully',
            'data': serializer.data
        }
        return response

    def put(self, request, pk=None, format=None):
        PurchaseBillDetails_to_update = PurchaseBillDetails.objects.get(pk=pk)
        serializer = PurchaseBillDetailsSerializer(instance=PurchaseBillDetails_to_update, data=request.data, partial=True)

        serializer.is_valid()
        serializer.save()
        response = Response()
        response.data = {
            'message': 'Purchase details Updated Successfully',
            'data': serializer.data
        }
        return response

    def delete(self, request, pk, format=None):
        PurchaseBillDetails_to_delete = PurchaseBillDetails.objects.get(pk=pk)
        PurchaseBillDetails_to_delete.delete()
        return Response({
            'message': 'Purchase details deleted successfully'
        })



# SaleBill
class SaleBillAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # filter_fields = ['name', 'category', 'subcategory', 'type']

    def get_object(self, pk):
        try:
            return SaleBill.objects.get(pk=pk)
        except SaleBill.DoesNotExist:
            raise

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = SaleBillSerializer(data)
            return Response(serializer.data)
        else:
            data = SaleBill.objects.all()
            serializer = SaleBillSerializer(data, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = SaleBillSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            'message': 'Sale Bill Add Successfully',
            'data': serializer.data
            }
        return response

    def put(self, request, pk=None, format=None):
        SaleBill_to_update = SaleBill.objects.get(pk=pk)
        serializer = SaleBillSerializer(instance=SaleBill_to_update, data=request.data, partial=True)

        serializer.is_valid()
        serializer.save()
        response = Response()
        response.data = {
            'message': 'Sale Bill Updated Successfully',
            'data': serializer.data
        }
        return response

    def delete(self, request, pk, format=None):
        SaleBill_to_delete = SaleBill.objects.get(pk=pk)
        SaleBill_to_delete.delete()
        return Response({
            'message': 'Sale Bill deleted successfully'
        })





# SaleBillDetails
class SaleBillDetailsAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # filter_fields = ['name', 'category', 'subcategory', 'type']

    def get_object(self, pk):
        try:
            return SaleBillDetails.objects.get(pk=pk)
        except SaleBillDetails.DoesNotExist:
            raise

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = SaleBillDetailsSerializer(data)
            return Response(serializer.data)
        else:
            data = SaleBillDetails.objects.all()
            serializer = SaleBillDetailsSerializer(data, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = SaleBillDetailsSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            'message': 'Sale details  Add Successfully',
            'data': serializer.data
            }
        return response

    def put(self, request, pk=None, format=None):
        SaleBillDetails_to_update = SaleBill.objects.get(pk=pk)
        serializer = SaleItemSerializer(instance=SaleBillDetails_to_update, data=request.data, partial=True)

        serializer.is_valid()
        serializer.save()
        response = Response()
        response.data = {
            'message': 'Sale Bill details Updated Successfully',
            'data': serializer.data
        }
        return response

    def delete(self, request, pk, format=None):
        SaleBillDetails_to_delete = SaleBillDetails.objects.get(pk=pk)
        SaleBillDetails_to_delete.delete()
        return Response({
            'message': 'Sale Item Bill deleted successfully'
        })


# SaleItem

class SaleItemAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # filter_fields = ['name', 'category', 'subcategory', 'type']

    def get_object(self, pk):
        try:
            return SaleItem.objects.get(pk=pk)
        except SaleItem.DoesNotExist:
            raise

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = SaleItemSerializer(data)
            return Response(serializer.data)
        else:
            data = SaleItem.objects.all()
            serializer = SaleItemSerializer(data, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = SaleItemSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            'message': 'Sale Item Bill Add Successfully',
            'data': serializer.data
            }
        return response

    def put(self, request, pk=None, format=None):
        SaleItem_to_update = SaleItem.objects.get(pk=pk)
        serializer = SaleItemSerializer(instance=SaleItem_to_update, data=request.data, partial=True)

        serializer.is_valid()
        serializer.save()
        response = Response()
        response.data = {
            'message': 'Sale Item Bill Updated Successfully',
            'data': serializer.data
        }
        return response

    def delete(self, request, pk, format=None):
        SaleItem_to_delete = SaleBill.objects.get(pk=pk)
        SaleItem_to_delete.delete()
        return Response({
            'message': 'Sale Item Bill deleted successfully'
        })
