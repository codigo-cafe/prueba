from apps.base.api import GeneralListApiView
from apps.reservations.api.serializers.general_serializers import RoomsSerializer

class RoomsListAPIView(GeneralListApiView):
	serializer_class = RoomsSerializer

