from django.shortcuts import render
from .models import Booking
from .serializers import BookingSerializer
from rest_framework import generics


# Create your views here.
class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


def homer(request):
    return render(request, '218_eventListener_notes2.html', {})



