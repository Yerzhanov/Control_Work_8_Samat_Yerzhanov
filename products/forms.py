from django import forms
from .models import Product, ProductCategory, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'image']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name', 'description']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user', 'product', 'description', 'rating']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти товар")