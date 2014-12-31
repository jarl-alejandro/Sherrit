from django.shortcuts import render
from django.http import HttpResponseRedirect
from apps.usuarios.models import Perfil
from apps.articulos.models import Articulo
from apps.articulos.forms import ArticuloForm

def home(request):
	perfil = Perfil.objects.filter(usuario = request.user)
	articulos = Articulo.objects.order_by('-votos').all()
	
	for p in perfil:
		avatar = p.avatar
	
	return render(request, "home.html", 
                      { 'avatar':avatar, 'articulos':articulos })

def articulo(request, slug):
	perfil = Perfil.objects.filter(usuario = request.user)
	articulo = Articulo.objects.get(slug = slug)

	for p in perfil:
		avatar = p.avatar
	
	return render(request, "articulo.html", 
                      { 'avatar':avatar, 'articulo':articulo })

def add(request):
	usuario = Perfil.objects.get(usuario = request.user)
	avatar = usuario.avatar
	if request.POST:
		form = ArticuloForm(request.POST)
		if form.is_valid():
			perfil = form.save(commit = False)
			perfil.creador = usuario
			perfil.save()
			return HttpResponseRedirect("/home/")
	else:
		form = ArticuloForm()

	return render(request, "add.html", 
                { 'form':form, 'avatar':avatar })
