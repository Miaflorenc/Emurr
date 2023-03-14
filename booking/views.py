from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from .service import BookingRepository
from .models import Booking
from .serializers import CreateBooking, GetBooking


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def BookingTable(request):
    if request.method == 'POST':
        serializer = CreateBooking(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def MyBooking(request, pk):
    B = BookingRepository()
    booking = B.Booking_by_pk(pk)
    serializer = GetBooking(booking, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def AllBooking(request):
    B = BookingRepository()
    booking = B.all_booking()
    serializer = GetBooking(booking, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteBooking(request, pk):
    B = BookingRepository()
    B.Delete_Booking(pk)
    return Response(status=status.HTTP_204_NO_CONTENT)
