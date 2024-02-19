from django.urls import path
from . import views


urlpatterns = [
    path('bookings', views.BookingView.as_view(), name="bookings"),
    path('', views.homer, name="homer"),
    path('book/', views.book, name="book"),
]