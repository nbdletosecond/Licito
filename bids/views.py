from django.http import HttpResponse
from django.shortcuts import render

def bids(request):
    context = {}
    return render(request, "bids/bids.html", context)