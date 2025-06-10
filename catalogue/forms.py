from django import forms

from catalogue.models import Item, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'slug']
        labels = {"title" : "Название категории", "slug" : "Адрес"}
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Введите название категории'
            }),
            "slug": forms.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Введите адрес'
            })
        }

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['id_category', 'title', 'description', 'price', 'img', 'slug']
        labels = {
            "id_category" : "Категория",
            "title" : "Название",
            "description" : "Описание",
            "price" : "Цена",
            "img" : "Изображение",
            "slug" : "Адрес"
        }
        widgets = {
            "id_category": forms.Select(attrs={'class': 'form-control mb-3'}),
            'title': forms.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Введите название товара'
            }),
            "description": forms.Textarea(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Описание товара'
            }),
            "price": forms.NumberInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Цена в рублях'
            }),
            "img": forms.ClearableFileInput(attrs={
                'class': 'form-control mb-3'
            }),
            "slug": forms.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Введите адрес'
            })
        }