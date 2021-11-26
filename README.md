# prueba_rest
 API con reservación de habitaciones para nuestros clientes
 Este proyecto incluye migraciones predeterminadas, también incluye una base de datos SQLITE con datos de ejemplo

 # admin
 Para administrar la información desde la interfaz gráfica se uso la ruta

                        http://localhost:8000/admin/

 podemos crear cualquier super usuario ejecutando en la consola el comando:

                        py manage.py createsuperuser

 llenamos los datos solicitados y podremos acceder desde el login

# API para clientes
 fue desarrollada con el decorador @api_view usando funciones

# API para reservaciones y habitaciones
 fue desarrollada con clases para mayor flexibilidad

# Lista de endpoints

1.- Lista de Clientes: (Client Api View)

                        http://localhost:8000/clients/client/

 endpoint creado para mostrar una lista de los clientes registrados con información detallada.
 Permite métodos GET, POST, OPTIONS

2.- Detalle del Cliente: (Client Detail Api View)

                        http://localhost:8000/clients/client/1/

 endpoint creado para visualizar la información de algun cliente, se usa como parámetro la Primary Key.
 Permite métodos GET, DELETE, PUT, OPTIONS

3.- Lista de Reservaciones: (Reservation List Api)

                        http://localhost:8000/reservations/reservation/list/

 endpoint creado para mostrar una lista de las reservaciones registradas con información detallada, incluyendo la relación con cliente y habitación.
 Permite métodos GET, HEAD, OPTIONS

4.- Lista de Habitaciones. (Rooms List Api)

                        http://localhost:8000/reservations/rooms/

 endpoint creado para mostrar una lista de las habitaciones registradas con información detallada, el registro de habitaciones solo está disponible desde el admin aunque también se podria haber realizado una API con sus respectivos endpoints para las habitaciones.
 Permite métodos GET, HEAD, OPTIONS

5.- Creación de Reservaciones: (Reservation Create Api)

                        http://localhost:8000/reservations/reservation/create/

 endpoint creado para registrar las reservaciones para un cliente registrado con anterioridad asi como también la habitación de la cual dispondrá.
 Permite métodos POST, OPTIONS

6.- Modificación de Reservaciones: (Reservation Update Api)

                        http://localhost:8000/reservations/reservation/update/1/

 endpoint creado para modificar alguna reservación, se usa como parámetro la Primary Key.
 Con PATCH recuperamos la información de la reservación y con PUT podemos guardar los cambios que se requieran.
 Permite métodos PUT, PATCH, OPTIONS


7.- Eliminación lógica de Reservaciones: (Reservation Destroy Api)

                        http://localhost:8000/reservations/reservation/destroy/1/

 endpoint creado para eliminar de manera lógica alguna reservación, se usa como parámetro la Primary Key.
 Al realizar la eliminación simplemente se modifica la columna sw (Switch) de True a False, entonces al realizar la lista de reservaciones el registro ya no se muestra ya que en la consulta se define listar todas las reservaciones que tengan la columna sw (Switch) igual a True.
 Permite métodos DELETE, OPTIONS
