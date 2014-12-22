from django.forms import ModelForm
from apps.usuarios.models import Perfil

class PerfilForm(ModelForm):
	class Meta:
		model = Perfil
		fields = ["avatar", "informacion"]