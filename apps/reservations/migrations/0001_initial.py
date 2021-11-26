# Generated by Django 3.2.9 on 2021-11-26 05:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sw', models.BooleanField(default=True, verbose_name='Estado de Eliminación')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('number', models.IntegerField(unique=True, verbose_name='Número de Habitación')),
                ('price', models.IntegerField(verbose_name='Precio por día de la Habitación')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Descripción de la Habitación')),
            ],
            options={
                'verbose_name': 'Habitación',
                'verbose_name_plural': 'Habitaciones',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sw', models.BooleanField(default=True, verbose_name='Estado de Eliminación')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('status', models.CharField(choices=[('Pe', 'Pendiente'), ('Pa', 'Pagado'), ('El', 'Eliminado')], default='Pe', max_length=2, verbose_name='Estado')),
                ('date_start', models.DateField(verbose_name='Fecha de Inicio')),
                ('date_end', models.DateField(verbose_name='Fecha de Finalización')),
                ('mount', models.IntegerField(verbose_name='Monto Total')),
                ('payment_method', models.CharField(choices=[('Ef', 'Efectivo'), ('Ta', 'Tarjeta'), ('Pa', 'Paypal')], max_length=2, verbose_name='Método de Pago')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Cliente')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.rooms', verbose_name='Habitación')),
            ],
            options={
                'verbose_name': 'Reservación',
                'verbose_name_plural': 'Reservaciones',
            },
        ),
        migrations.CreateModel(
            name='HistoricalRooms',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('sw', models.BooleanField(default=True, verbose_name='Estado de Eliminación')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('delete_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('number', models.IntegerField(db_index=True, verbose_name='Número de Habitación')),
                ('price', models.IntegerField(verbose_name='Precio por día de la Habitación')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Descripción de la Habitación')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Habitación',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalReservation',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('sw', models.BooleanField(default=True, verbose_name='Estado de Eliminación')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('delete_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('status', models.CharField(choices=[('Pe', 'Pendiente'), ('Pa', 'Pagado'), ('El', 'Eliminado')], default='Pe', max_length=2, verbose_name='Estado')),
                ('date_start', models.DateField(verbose_name='Fecha de Inicio')),
                ('date_end', models.DateField(verbose_name='Fecha de Finalización')),
                ('mount', models.IntegerField(verbose_name='Monto Total')),
                ('payment_method', models.CharField(choices=[('Ef', 'Efectivo'), ('Ta', 'Tarjeta'), ('Pa', 'Paypal')], max_length=2, verbose_name='Método de Pago')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('client', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Cliente')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='reservations.rooms', verbose_name='Habitación')),
            ],
            options={
                'verbose_name': 'historical Reservación',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
