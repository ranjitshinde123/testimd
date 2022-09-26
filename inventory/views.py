

from rest_framework.response import Response

from . serializers import *

from .models import Stock
from .serializers import StockSerializer, userSerializers
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication




# ResisterApi
class Register(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = userSerializers(data=request.data)
        print(request)

        if not serializer.is_valid():
            return Response({'status': 404, 'errors': serializer.errors, 'message': 'Something wrong '})
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        # create token
        # token_user ,_=Token.objects.get_or_create(user=user)
        refresh = RefreshToken.for_user(user=user)

        return Response({'status': 200, 'payload': serializer.data, 'refresh': str(refresh),
                         'access': str(refresh.access_token), 'message': 'your data saved'})

#
#
# @api_view(['POST'])
# def send_otp(request):
#     data=request.data
#
#     if data.get('phone_number') is None:
#         return Response({
#             'status':400,
#             'message':'key phone_number is required'
#         })
#     if data.get('password') is None:
#         return Response({
#             'status':400,
#             'message':'key password  is required'
#         })
#     user = User.objects.get(
#         phone_number=data.get('phone_number'),
#         otp=send_otp_to_phone(data.get('phone_number')))
#     user.set_password=data.get('set_password')
#     user.save()
#     return Response({
#         'status':200,
#         'message':'OTP sent'
#     })
# @api_view(['POST'])
# def verify_otp(request):
#     data=request.data
#
#     if data.get('phone_number') is None:
#         return Response({
#             'status': 400,
#             'message': 'key phone_number is required'
#         })
#     if data.get('otp') is None:
#         return Response({
#             'status': 400,
#             'message': 'key otp  is required'
#         })
#
#     try:
#         user_obj = User.objects.create(phone_number=data.get('phone_number'))
#
#     except Exception as e:
#         return Response({
#             'status':400,'message':'Invalid phone'
#         })
#
#     if user_obj.otp==data.get('otp'):
#         return Response({
#             'status':200,'message':'otp matched'
#         })
#
#     return Response({
#         'status': 400, 'message': 'Invalid otp'})
#
#
#


class StockAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_fields = ['name', 'category', 'subcategory', 'type']

    def get_object(self, pk):
        try:
            return Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            raise

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = StockSerializer(data)
            return Response(serializer.data)
        else:
            data = Stock.objects.all()
            serializer = StockSerializer(data, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = StockSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            'message': 'Stock Add Successfully',
            'data': serializer.data
        }
        return response

    def put(self, request, pk=None, format=None):
        Stock_to_update = Stock.objects.get(pk=pk)
        serializer = StockSerializer(instance=Stock_to_update, data=request.data, partial=True)

        serializer.is_valid()
        serializer.save()
        response = Response()
        response.data = {
            'message': 'Stock Updated Successfully',
            'data': serializer.data
        }
        return response

    def delete(self, request, pk, format=None):
        Stock_to_delete = Stock.objects.get(pk=pk)
        Stock_to_delete.delete()
        return Response({
            'message': 'Stock deleted successfully'
        })


