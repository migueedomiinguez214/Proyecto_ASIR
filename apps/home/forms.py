from django import forms
from .models import *

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['titulo', 'urgencia', 'descripcion']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'urgencia': forms.Select(attrs={'class': 'form-select'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


class TicketSuperuserForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'

class AlmacenForm(forms.ModelForm):
    class Meta:
        model = Almacen
        fields = '__all__'