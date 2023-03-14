from django.contrib import admin
from django.urls import path, include
from booking import views


urlpatterns = [
     path('create_booking/', views.BookingTable),
     path('get_booking/<str:pk>/', views.MyBooking),
     path('get_all_booking/', views.AllBooking),
     path('delete_booking/<str:pk>', views.DeleteBooking),
]