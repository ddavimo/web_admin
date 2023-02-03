
from django import forms
from .models import Cafe, GeeksModel


class GeeksForm(forms.ModelForm):

    class Meta:
        model = GeeksModel

        fields = [
            "title",
            "description",
        ]


class CafeForm(forms.ModelForm):

    FAVORITE_COLORS_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]

    # descripcion = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    # name = forms.ChoiceField(widget=forms.RadioSelect,
    #                          choices=FAVORITE_COLORS_CHOICES)

    class Meta:
        model = Cafe
        fields = '__all__'

        # exclude = ['nombre']   # Para excluir los acmpos que no quiero que se vean en la plantilla

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ingrese el nombre',
                    'id': 'id_nombre',
                    'name': 'nombre'
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'descripcion del producto',
                    'id': 'id_descrip',
                    'name': 'descrip'
                }
            ),
            'codCafe': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Codigo del producto',
                    'id': 'id_cod',
                    'name': 'codcafe'
                }
            ),
        }
