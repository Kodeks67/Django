from django.shortcuts import render
from rest_framework import generics
# Create your views here.

from .serializers import ComicsSerializer
from account.models import Comics


class ComicsApiView(generics.ListAPIView):
    queryset = Comics.objects.all()
    serializer_class = ComicsSerializer
