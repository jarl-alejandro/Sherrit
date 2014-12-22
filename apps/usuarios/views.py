from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth import logout

from apps.usuarios.forms import PerfilForm
from apps.usuarios.models import Perfil

def login(request):
	return render(request, "login.html")

def error(request):
	return render(request, "error.html")

def logOut(request):
	logout(request)
	return HttpResponseRedirect('/')

def nuevo_usuario(request):
	if request.POST:
		form = PerfilForm(request.POST, request.FILES)
		if form.is_valid():
			perfil = form.save(commit = False)
			perfil.usuario = request.user
			perfil.save()
			return HttpResponseRedirect("/home")
	else:
		form = PerfilForm()
	return render(request, "nuevousuario.html", {'form':form })


