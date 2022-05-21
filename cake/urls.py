from django.urls import path

from cake.views import home, contact, shop, about, SweetsListView, OrderCreateView, SubscriptionCreateView

urlpatterns = [
    path('', SweetsListView.as_view(), name='home'),
    path('create/', OrderCreateView.as_view(), name='create'),
    path('subscription/', SubscriptionCreateView.as_view(), name='subscription'),
    path('about/', about, name='about'),
    path('shop/', shop, name='shop'),
    path('contact/', contact, name='contact'),
]
