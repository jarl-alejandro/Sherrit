from django.shortcuts import render
from apps.usuarios.models import Perfil
from apps.articulos.models import Articulo

def home(request):
	perfil = Perfil.objects.filter(usuario = request.user)
	articulos = Articulo.objects.order_by('-votos').all()
	
	for p in perfil:
		avatar = p.avatar
	
	return render(request, "home.html", { 'avatar':avatar, 'articulos':articulos })

def articulo(request, slug):
	perfil = Perfil.objects.filter(usuario = request.user)
	articulo = Articulo.objects.get(slug = slug)

	for p in perfil:
		avatar = p.avatar
	
	return render(request, "articulo.html", { 'avatar':avatar, 'articulo':articulo })