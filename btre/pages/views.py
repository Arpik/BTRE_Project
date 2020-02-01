from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)[:3]

    context = {
        'listings': listings
    }

    return render(request, 'pages/index.htm', context)

def about(request):
    return render(request, 'pages/about.htm') 