from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel
from apps.clients.models import Client

# Create your models here.
class Rooms(BaseModel):
	number = models.IntegerField('Número de Habitación', unique = True, blank = False, null = False)
	price = models.IntegerField('Precio por día de la Habitación', blank = False, null = False)
	description = models.CharField('Descripción de la Habitación', max_length = 255, null = True, blank = True)
	historical = HistoricalRecords()

	@property
	def _history_user(self):
		return self.changed_by

	@_history_user.setter
	def _history_user(self, value):
		self.changed_by = value

	class Meta:
		verbose_name = 'Habitación'
		verbose_name_plural = 'Habitaciones'

	def __str__(self):
		return str(self.number)

class Reservation(BaseModel):
	PENDIENTE = 'Pe'
	PAGADO = 'Pa'
	ELIMINADO = 'El'
	STATUS_CHOICES = [
		(PENDIENTE, 'Pendiente'),
		(PAGADO, 'Pagado'),
		(ELIMINADO, 'Eliminado'),
	]

	status = models.CharField(
		'Estado',
        max_length = 2,
        choices = STATUS_CHOICES,
        default = PENDIENTE,
    )

	date_start = models.DateField(
		'Fecha de Inicio',
		auto_now = False,
		auto_now_add = False
	)

	date_end = models.DateField(
		'Fecha de Finalización',
		auto_now = False,
		auto_now_add = False
	)

	mount = models.IntegerField('Monto Total', blank = False, null = False)

	EFECTIVO = 'Ef'
	TARJETA = 'Ta'
	PAYPAL = 'Pa'
	PAYMENT_METHOD_CHOICES = [
		(EFECTIVO, 'Efectivo'),
		(TARJETA, 'Tarjeta'),
		(PAYPAL, 'Paypal'),
	]

	payment_method = models.CharField(
		'Método de Pago',
        max_length = 2,
        choices = PAYMENT_METHOD_CHOICES,
    )

	client = models.ForeignKey(Client, on_delete = models.CASCADE, verbose_name = 'Cliente')
	room = models.ForeignKey(Rooms, on_delete = models.CASCADE, verbose_name = 'Habitación')
	historical = HistoricalRecords()

	@property
	def _history_user(self):
		return self.changed_by

	@_history_user.setter
	def _history_user(self, value):
		self.changed_by = value

	class Meta:
		verbose_name = 'Reservación'
		verbose_name_plural = 'Reservaciones'

	def __str__(self):
		return str(self.date_start)