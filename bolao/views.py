from django.shortcuts import render
from .models import Jogo, Aposta
#from .forms import PostForm

# Create your views here.

def jogos_list(request):
	jogos = Jogo.objects.all()
	return render(request, 'bolao/jogos_list.html', {'jogos': jogos})

def classificacao(request):
	return render(request, 'bolao/classificacao.html', {})

def rodadas_anteriores(request):
	return render(request, 'bolao/rodadas_anteriores.html', {})