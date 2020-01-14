from django.shortcuts import render

# Create your views here.

def jogos_list(request):
	return render(request, 'bolao/jogos_list.html', {})