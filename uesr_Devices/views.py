from django.shortcuts import render
from .serializer import UserDeveicSerializer
from .models import UserDevice
from rest_framework import viewsets
from django.http import Http404

class UserDeviceViewsets(viewsets.ModelViewSet):
    queryset = UserDevice.objects.all()
    serializer_class = UserDeveicSerializer


    def get_queryset(self):
        params_id = self.request.query_params.get("params_id")
        if params_id is not None:
            try:
                return UserDevice.objects.filter(id=params_id)
            except UserDevice.DoesNotExist:
                return Http404("User Device does not exist for gaven in params id ")
        return UserDevice.objects.all()