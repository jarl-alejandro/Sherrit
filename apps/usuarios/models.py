from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
	usuario = models.OneToOneField(User)
	avatar = models.ImageField(upload_to = 'avatar')
	informacion = models.TextField(blank = True)

	class Meta:
		verbose_name = u'Perfile'

	def __unicode__(self):
		return self.usuario.username