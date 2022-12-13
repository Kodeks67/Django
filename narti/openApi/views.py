from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

from .serializers import ComicsSerializer, LanguageSerializer
from account.models import Comics, Language


class ComicsApiView(APIView):

    def get(self, request):
        w = Comics.objects.all()
        return Response({'comics': ComicsSerializer(w, many=True).data})

    def post(self, request):
        serializer = ComicsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'comics': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Comics.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = ComicsSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"comics": serializer.data})


class LangsApiView(APIView):
    def get(self, request):
        lst = Language.objects.all()
        return Response({'languages': LanguageSerializer(lst, many=True).data})
