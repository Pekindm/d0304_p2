from django.conf import settings
from django.shortcuts import render
from django.views import View
import tours.data as data
from django.http import Http404
import random


def main_view(request):
    try:
        context = {
            'title': data.title,
            'subtitle': data.subtitle,
            'description': data.description,
            'tours': [{'id': i, **data.tours[i]} for i in random.sample(sorted(data.tours), 6)],
        }
    except KeyError:
        raise Http404
    return render(request, 'tours/index.html', context=context)


def departure_view(request, departure):
    try:
        tours_list = [{'id': i, **data.tours[i]} for i in data.tours if data.tours[i]['departure'] == departure]
        price_list = [tour['price'] for tour in tours_list]
        context = {
            "departure": data.departures[departure],
            'tours': tours_list,
            'min_price': '{0:,}'.format(min(price_list)).replace(',', ' '),
            'max_price': '{0:,}'.format(max(price_list)).replace(',', ' '),
            'min_nights': min([tour['nights'] for tour in tours_list]),
            'max_nights': max([tour['nights'] for tour in tours_list]),
            'len': len(tours_list)
        }
    except KeyError:
        raise Http404
    return render(request, 'tours/departure.html', context=context)


def tour_view(request, id):
    try:
        context = {
            'tour': data.tours[id],
            'departure': data.departures[data.tours[id]['departure']]
        }
    except KeyError:
        raise Http404
    return render(request, 'tours/tour.html', context=context)
