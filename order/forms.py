from django import forms
from django.forms import Select

from catalogue.models import Item
from order.models import Order

class ItemSelect(Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if value:
            option['attrs']['data-price'] = value.instance.price + 200
        return option

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['id_Item', 'start', 'end', 'address', 'price']
        labels = {
            "id_Item" : "Оборудование",
            "start" : "От",
            "end" : "До",
            "address" : "Адрес",
            "price" : "Итоговая цена"
        }
        widgets = {
            'id_Item' : ItemSelect(attrs={
                'class': 'form-control mb-3',
                'id' : 'myselect',
                'onchange' : 'changePrice()',
                'data-price' : ''
            }),
            'start': forms.DateTimeInput(attrs={
                'class': 'form-control mb-3',
                'type': 'datetime-local'
            }),
            'end': forms.DateTimeInput(attrs={
                'class': 'form-control mb-3',
                'type': 'datetime-local' 
            }),
            'address' : forms.TextInput(attrs = {
                'class': 'form-control mb-3',
                'placeholder': "Введите адрес доставки"
            }),
            'price' : forms.NumberInput(attrs = {
                'class': 'form-control mb-3',
                'placeholder': 'Итоговая цена',
                'id' : 'price',
                'readonly': True
            })
        }