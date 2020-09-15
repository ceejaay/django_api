from django.shortcuts import render
from .models import Subscription
# Create your views here.

from django.views.generic import (
        CreateView,
        ListView,
        )



class SubscriptionListView(ListView):
    model = Subscription
