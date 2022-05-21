from django.shortcuts import render
from django.views.generic import ListView, CreateView

from cake.forms import OrderForm, SubscriptionForm
from cake.models import Sweets, Order, Subscription


class SweetsListView(ListView):
    model = Sweets
    template_name = "cake/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm()
        context['subscription'] = SubscriptionForm()
        return context


class OrderCreateView(CreateView):
    model = Order
    template_name = "cake/index.html"
    form_class = OrderForm
    success_url = "/"


class SubscriptionCreateView(CreateView):
    model = Subscription
    template_name = "cake/index.html"
    form_class = SubscriptionForm
    success_url = "/"


def home(request):
    return render(request, 'cake/index.html')


def about(request):
    return render(request, 'cake/about.html')


def shop(request):
    return render(request, 'cake/shop.html')


def contact(request):
    return render(request, 'cake/contact.html')
