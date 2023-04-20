import stripe

from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order, OrderItem
from .serializers import OrderSerializer

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permission.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer 

    if serializer.is_valid():
        stripe.api_key = settings.STRIPE_SECRET_KEY
        paid_amount = sum(item.get('quantity') * item.get('product').price for item in serializer.validated_data['items'])

        try:
            charge = stripe.Charge.create(
                amount=int(paid_amount * 100)
                currency='USD'
                description='charge from Pristine Apparels'
                sources=serializer.validated_data['stripe_token']
            
            )

            serializer.save(user=request.user, paid_amount=paid_amount)

            return Response(serializer.data, status=status.HTTP_200_CREATED)
        except Exception:
            return Response(serializer.errors, status=status.400_BAD_REQUEST)
        
    return Response(serializer.errors, status=status.400_BAD_REQUEST)

        
