from rest_framework import generics

from .models import Res
from .serializers import ResSerializer


class ListRes(generics.ListCreateAPIView):
    queryset = Res.objects.all()
    serializer_class = ResSerializer


class DetailRes(generics.RetrieveUpdateDestroyAPIView):
    queryset = Res.objects.all()
    serializer_class = ResSerializer
