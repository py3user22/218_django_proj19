from django.urls import path
from . import views


urlpatterns = [
    path('bookings', views.BookingView.as_view()),
    path('', views.homer),
]