from django import forms

from cake.models import Order, Subscription


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Атыңыз"}),
            "phone": forms.TextInput(attrs={"placeholder": "Телефонуңуз"}),
            "address": forms.TextInput(attrs={"placeholder": "Адрес"}),
            "messages": forms.Textarea(
                attrs={"placeholder": "Талаптарыңызды жазыңыз", 'class': 'form-control', "rows": 5})
        }


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ('email',)
        widgets = {
             "email": forms.EmailInput(attrs={"placeholder": "E-mail"})
         }
