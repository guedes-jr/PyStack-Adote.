from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.messages import constants
from divulgar.models import Pet, Raca
from django.http import HttpResponse
from django.contrib import messages
from .models import PedidoAdocao
from datetime import datetime
from django.core.mail import send_mail

@login_required
def listar_pets(request):
    if request.method == "GET":
        pets = Pet.objects.filter(status='P')
        racas = Raca.objects.all()

        cidade = request.GET.get('cidade')
        raca_filter = request.GET.get('raca')

        if cidade:
            pets = pets.filter(cidade__icontains=cidade)
        
        if raca_filter:
            pets = pets.filter(raca__id=raca_filter)
            raca_filter = Raca.objects.get(id=raca_filter)

        return render(request, 'listar_pets.html', {
                                                    'pets': pets,
                                                    'racas': racas,
                                                    'cidade': cidade,
                                                    'raca_filter': raca_filter
                                                  })
@login_required
def pedido_adocao(request, id_pet):
    pet = Pet.objects.filter(id=id_pet, status='P')
    if not pet.exists:
        messages.add_message(request, constants.WARNING, 'Esse pet já foi adotado!')
        return redirect('/adotar')

    pedido = PedidoAdocao(pet=pet.first(),
                          usuario=request.user,
                          data=datetime.now())
    pedido.save()
    messages.add_message(request, constants.SUCCESS, 'Pedido de adição realizado com sucesso!')

    return redirect('/adotar')

@login_required
def processa_pedido_adocao(request, id_pedido):
    status = request.GET.get('status')
    pedido = PedidoAdocao.objects.get(id=id_pedido)

    if status == 'A':
        pedido.status = 'AP'
        string = '''olá! Sua adoção foi aprovada com sucesso!....'''
    elif status == 'R':
        pedido.status = 'R'
        string = '''olá! Sua adoção foi Recusada!'''

    pedido.save()

    email = send_mail(
        'Sua adoção foi processada',
        string,
        'meuemail@.gmail.com',
        [
            pedido.usuario.email,
        ]
    )

    messages.add_message(request, constants.SUCCESS, 'Pedido de adoção processado com sucesso!')
    return redirect('/divulgar/ver_pedido_adocao')