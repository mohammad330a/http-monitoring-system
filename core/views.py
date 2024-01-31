from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from core.serializers import ServerModelSerializer
from core.models import Server


class ServerRegisterAPI(CreateAPIView):
    serializer_class = ServerModelSerializer
    queryset = Server.objects.all()


class ServerStatusAPI(RetrieveAPIView):
    serializer_class = ServerModelSerializer
    queryset = Server.objects.all()

    def get_object(self):
        return get_object_or_404(Server, pk=self.request.query_params.get('pk'))


class ServerListAPI(ListAPIView):
    serializer_class = ServerModelSerializer
    queryset = Server.objects.all()
