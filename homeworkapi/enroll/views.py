from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *

# Create your views here.
class FacultyViewSet(viewsets.ModelViewSet):
    queryset = FacultyInfo.objects.all()
    serializer_class = FactulySerializer
    permission_classes = [IsAuthenticated]

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = DepartmentInfo.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = SubjectInfo.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]

class EnrollViewSet(viewsets.ModelViewSet):
    queryset = EnrollInfo.objects.all()
    serializer_class = EnrollSerializer
    permission_classes = [IsAuthenticated]

