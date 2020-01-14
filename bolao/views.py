from django.shortcuts import render
from .models import Jogo, Aposta

# Create your views here.

def jogos_list(request):
	jogos = Jogo.objects.all()
	return render(request, 'bolao/jogos_list.html', {'jogos': jogos})