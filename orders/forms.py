from django import forms
from .models import Order


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["full_name", "email", "phone", "address", "city", "state", "pincode", "payment_method"]
        widgets = {
            "address": forms.Textarea(attrs={"rows": 3}),
        }
