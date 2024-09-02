from django import forms

from .models import Socio, Deporte, Instalacion

class SocioForm(forms.ModelForm):
    deportes = forms.ModelMultipleChoiceField(
        queryset=Deporte.objects.filter(disponible=True),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Socio
        fields = "__all__"
        widgets = {
            'año_nacimiento': forms.NumberInput(attrs={'min': 1900, 'max': 2022})
        }

class DeporteForm(forms.ModelForm):
    instalaciones = forms.ModelMultipleChoiceField(
        queryset=Instalacion.objects.filter(disponible=True),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Deporte
        fields = "__all__"

class InstalacionForm(forms.ModelForm):
    class Meta:
        model = Instalacion
        fields = "__all__"
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'cols': 15})
        }


