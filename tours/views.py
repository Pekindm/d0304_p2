from django.conf import settings
from django.shortcuts import render
from django.views import View


def main_view(request):
    return render(request, 'tours/index.html')


def departure_view(request, departure):
    context = {
        "departure": departure
    }
    return render(request, 'tours/departure.html', context=context)


def tour_view(request, id):
    context = {
        "id": id
    }
    return render(request, 'tours/tour.html', context=context)
