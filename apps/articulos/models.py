from django.db import models
from django.template.defaultfilters import slugify
from apps.usuarios.models import Perfil

class Articulo(models.Model):
	creador = models.ForeignKey(Perfil)
	titulo = models.CharField(max_length = 140)
	contenido = models.TextField(default = '')
	fecha = models.DateTimeField(auto_now_add = True)
	votos = models.IntegerField(default = 0)
	slug = models.SlugField(editable = False)

	def __unicode__(self):
		return "%s (%s)" % (self.titulo, self.creador.usuario.username)

	def save(self, *args, **kargs):
		if not self.id:
			self.slug = slugify(self.titulo)
		super(Articulo, self).save(*args, **kargs)