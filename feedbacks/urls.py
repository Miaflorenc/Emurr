from django.contrib import admin
from django.urls import path, include
from feedbacks import views
urlpatterns = [
    path('feedbacks/', views.FeedbacksList),
    path('feeds-create/', views.FeedbacksCreate),
]