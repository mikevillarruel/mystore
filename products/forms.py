from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = "form-control"

        self.fields['discount'].widget.attrs["max"] = 100
        self.fields['discount'].widget.attrs["min"] = 1

        self.fields['stock'].widget.attrs["min"] = 1

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['created_at', 'modified_at', 'deleted_at', 'images', 'user']


class ProductCreationForm(ProductForm):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        'id': 'input',
        'multiple': True,
    }))


class ImagesCreationForm(forms.Form):
    add_images = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        'id': 'input',
        'class': 'form-control',
        'multiple': True,
    }))
