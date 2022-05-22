from django import forms
from django.utils.translation import ugettext_lazy as _

from cake.models import Order, Subscription, Feedback


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": _("Атыңыз")}),
            "phone": forms.TextInput(attrs={"placeholder": _("Телефонуңуз"), 'name': 'phone'}),
            "address": forms.TextInput(attrs={"placeholder": _("Адрес")}),
            "messages": forms.Textarea(
                attrs={"placeholder": _("Талаптарыңызды жазыңыз"), 'class': 'form-control', "rows": 5})
        }


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ('email',)
        widgets = {
            "email": forms.EmailInput(attrs={"placeholder": "E-mail"})
        }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={'placeholder': _('Атыңыз')}),
            "email": forms.TextInput(attrs={'placeholder': _('E-mail')}),
            "messages": forms.Textarea(attrs={'placeholder': _('Кат')}),
        }
