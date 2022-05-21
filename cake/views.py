from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView

from cake.forms import OrderForm, SubscriptionForm, FeedbackForm
from cake.models import Sweets, Order, Subscription, Feedback


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


def about(request):
    return render(request, 'cake/about.html')


class FeedbackCreateView(CreateView):
    model = Feedback
    template_name = "cake/contact.html"
    form_class = FeedbackForm
    success_url = "/"


class ShopListView(ListView):
    model = Sweets
    template_name = "cake/shop.html"
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sweet_count'] = Sweets.objects.count()
        return context

