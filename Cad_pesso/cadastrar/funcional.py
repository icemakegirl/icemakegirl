from .models import cadastro
from .forms import *
# Create your views here.
def total_pessoa():
    pessoas=cadastro.objects.all()
    conta_quantia=0
    for i in pessoas:
        conta_quantia+= i.quantia
        
    return conta_quantia
def media_quantidade():
    pessoas=cadastro.objects.all()
    total=total_pessoa()
    cont=0
    for i in pessoas:
        cont+=1
        
    return (total/cont)