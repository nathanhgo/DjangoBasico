from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa

# Create your views here.
def ver_produto(request):
    if request.method == 'GET':
        titulo = 'Ver Produto 🖥'
        return render(request, 'ver_produto.html', {'titulo': titulo})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        
        # Registrar
        # pessoa = Pessoa(nome=nome, idade=idade)
        # pessoa.save()

        # Ler
        # pessoas = Pessoa.objects.all()
        # print(pessoas[0])

        #Filtrar
        pessoas = Pessoa.objects.filter(nome=nome)

        return HttpResponse(pessoas)


def inserir_produto(request):
    return HttpResponse('Estou no inserir')