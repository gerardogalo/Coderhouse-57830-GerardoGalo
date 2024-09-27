from django import forms
from django.forms import DateInput
from .models import Socio, Deporte, Instalacion
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

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
            'fecha_nacimiento': DateInput(attrs={'type': 'date'}),
        }
    
    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        if fecha_nacimiento:
            # Comprueba si la fecha de nacimiento es más reciente que hace un mes
            if fecha_nacimiento > (timezone.now().date() - timedelta(days=30)):
                raise ValidationError("Fecha de nacimiento invalida. El socio debe tener al menos un mes de edad")
        return fecha_nacimiento

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


