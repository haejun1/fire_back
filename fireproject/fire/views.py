from django.shortcuts import render
from .models import *
from .forms import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#교내 공모전 목록
class FireAPIView(APIView):
    def get(self, request):
        fire = Fire.objects.all()
        serializer = FireSerializer(fire, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        fireForm = FireForm(request.data)
        if fireForm.is_valid():
            fireForm.save()
            return Response(fireForm.cleaned_data, status=status.HTTP_201_CREATED)
        return Response(fireForm.errors, status=status.HTTP_400_BAD_REQUEST)