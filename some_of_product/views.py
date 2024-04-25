from django.shortcuts import render
from .models import BennerSection
from .serializer import BennerSerializer
from rest_framework import viewsets


class BennerViewset(viewsets.ModelViewSet):
    queryset = BennerSection.objects.all()
    serializer_class = BennerSerializer

    