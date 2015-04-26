from django.shortcuts import render, HttpResponse
from .forms import EventoForm
from lugares.models import Lugar
from django.views.generic import CreateView

from django.template.response import TemplateResponse

def home(request):
	response = TemplateResponse(request, 'index.html', {})
	return response

"""
def crearEvento(request):
	if request.method == 'POST':
		form = EventoForm(request.POST)
		if form.is_valid():
			form.save()

	else:
		form = EventoForm()

	return render(request, 'crearEvento.html', {'form':form})
"""

class crearLugar(CreateView):
	template_name = 'crearLugar.html'
	model = Lugar
	success_url = '/'