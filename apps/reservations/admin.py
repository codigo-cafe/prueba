from django.contrib import admin
from apps.reservations.models import *

# Register your models here.
class RoomsAdmin(admin.ModelAdmin):
	list_display = ('id', 'number')

class ReservationAdmin(admin.ModelAdmin):
	list_display = ('id', 'date_start', 'date_end')

admin.site.register(Rooms, RoomsAdmin)
admin.site.register(Reservation, ReservationAdmin)