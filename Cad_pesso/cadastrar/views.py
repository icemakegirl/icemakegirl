from django.shortcuts import render
import matplotlib.pyplot as plt
from .models import cadastro
from .forms import *
from .funcional import *
# Create your views here.

def Home(request):
    recebe=0
    media=0
    total=0
    init=cadastro.objects.all()
    if (request.method=='POST'):
        form=cambio(request.POST or None, request.FILES or None)
        form1=media_cambio(request.POST or None, request.FILES or None)
        form2=total_cambio(request.POST or None, request.FILES or None)
        if (form.is_valid()):
            quanti = form.cleaned_data["quantia"]
            identifica = form.cleaned_data["id"]
            print(identifica)
            #pegar o id dar um filter, depois pegar a variavel.quantidade e multiplicar pela quanti
            retorno=cadastro.objects.get(id=identifica)
            recebe=round(quanti*retorno.quantia,2)
        if(form1.is_valid()):
            med_ia= form1.cleaned_data["media"]
            if(med_ia=='media'):
                media=round(media_quantidade(),2)
        if(form2.is_valid()):
            total_quantidade= form2.cleaned_data["total"]
            if(total_quantidade=='total'):
                total=total_pessoa()
        
            
    form=cambio()   
    form1=media_cambio()
    form2=total_cambio()
    return render(request, "cadastrar/Home.html", {'home':init,'form':form,'form1':form1,'form2':form2,'retorne':recebe,'total':total,'media':media})


def cadastro_pessoas(request):
    init=cadastro.objects.last()
    if (request.method=='POST'):
        print("Request.POST")
        formulario = cadFormulario(request.POST or None, request.FILES or None)
        if (formulario.is_valid()):
            print("firmulario.is_valid")
            name= formulario.cleaned_data["nome"]
            date= formulario.cleaned_data["data"]
            quanti = formulario.cleaned_data["quantia"]
            novacad = cadastro(nome=name, data=date,quantia=quanti)
            novacad.save()
            

    formulario = cadFormulario()
    return render(request, "cadastrar/cadastro_pessoas.html", {'home':init,'form':formulario})


def deletar(request,pessoa_id):
    cadastro.objects.get(id=pessoa_id).delete()
    return  render(request, "cadastrar/deletar.html")


def update(request,pessoa_id):
    id_cadastro=cadastro.objects.get(id=pessoa_id)
    print((id_cadastro.quantia))
    form =cadFormulario(instance =id_cadastro)
    if request.method=='POST':
        form =cadFormulario(request.POST,instance=id_cadastro)
        if form.is_valid():
            form.save()
        
    return render(request, "cadastrar/update.html", {'form':form,'identifica':id_cadastro})

def exibe_grafico(request):
    pessoas=cadastro.objects.all()
    x=[]
    y=[]
    for i in pessoas:
        x.append(i.nome)
        y.append(i.quantia)
    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(221)
    ax.bar(x, y,color='#00ff77')
    plt.savefig('static/graficos_pessoas.png', transparent=True)
    return render(request, "cadastrar/exibe_grafico.html", {'Plt':plt})
