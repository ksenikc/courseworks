from .models import Orders
from django.forms import ModelForm, TextInput, Textarea


class ProductForm(ModelForm):
    class Meta:
        model = Orders
        fields = ["created", "description"]
        widgets = {
            "created": TextInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }
