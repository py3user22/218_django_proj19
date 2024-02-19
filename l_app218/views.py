from django.views.decorators.csrf import csrf_exempt
from .serializers import BookingSerializer
from django.shortcuts import render
from rest_framework import generics
from .forms import BookingForm
from .models import Booking


# Create your views here.
class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


def homer(request):
    return render(request, '218_eventListener_notes2.html', {})


def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'book.html', {'form': form})

