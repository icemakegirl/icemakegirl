from django import forms
from .models import *

class dataformatada(forms.DateInput):
    input_type= 'date'

class media_cambio(forms.Form):
    media = forms.CharField(max_length=10)
    
class total_cambio(forms.Form):
    total = forms.CharField(max_length=10)    
    
class cadFormulario(forms.ModelForm):
    class Meta:
        model = cadastro
        fields = ['nome','quantia','data']
    nome = forms.CharField(max_length=200,label='Nome')
    quantia = forms.DecimalField(max_digits=100,decimal_places=2,label='Quantidade')
    data=forms.DateField(widget=dataformatada(attrs={'class': 'form-control'}),label='Data')

class cambio(forms.ModelForm):
    class Meta:
        model = cadastro
        fields = ['id']
    id=forms.IntegerField(label='ID')
    quantia = forms.DecimalField(max_digits=100,decimal_places=2,label='Quantidade')