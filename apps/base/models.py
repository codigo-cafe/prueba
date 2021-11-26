from django.db import models

# Create your models here.
class BaseModel(models.Model):
	"""docstring for BaseModel"""
	id = models.AutoField(primary_key = True)
	sw = models.BooleanField('Estado de Eliminación', default = True)
	created_date = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)
	modified_date = models.DateField('Fecha de Modificación', auto_now = True, auto_now_add = False)
	delete_date = models.DateField('Fecha de Eliminación', auto_now = True, auto_now_add = False)

	class Meta:
		abstract = True
		verbose_name = 'Modelo Base'
		verbose_name_plural = 'Modelos Base'