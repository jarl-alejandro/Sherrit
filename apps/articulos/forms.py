from django.forms import ModelForm
from apps.articulos.models import Articulo

class ArticuloForm(ModelForm):
	class Meta:
		model = Articulo
		exclude = ["slug", 'creador', 'votos']