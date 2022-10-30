from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from account.models import Account
from .serializers import *
from .models import *

@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def addenroll(request):

    if request.method == 'POST':
        serializer = EnrollSerializer(data=request.data)
        res = {}
        if serializer.is_valid():
            enroll = serializer.save()
            res['status'] = 'Success'
            res['message'] = 'Register successful'
            return Response(res)
        else:
            return Response(serializer.errors)

@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def addfaculty(request):

    if request.method == 'POST':
        serializer = FactulySerializer(data=request.data)
        res = {}
        if serializer.is_valid():
            enroll = serializer.save()
            res['status'] = 'Success'
            res['message'] = 'Register successful'
            return Response(res)
        else:
            return Response(serializer.errors)

@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def adddept(request):

    if request.method == 'POST':
        serializer = DepartmentSerializer(data=request.data)
        res = {}
        if serializer.is_valid():
            enroll = serializer.save()
            res['status'] = 'Success'
            res['message'] = 'Register successful'
            return Response(res)
        else:
            return Response(serializer.errors)

@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def addsubject(request):

    if request.method == 'POST':
        serializer = SubjectSerializer(data=request.data)
        res = {}
        if serializer.is_valid():
            enroll = serializer.save()
            res['status'] = 'Success'
            res['message'] = 'Register successful'
            return Response(res)
        else:
            return Response(serializer.errors)

@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def updateenroll(request):

    if request.method == 'POST':
        pk = request.data['nrl_id']
        enroll = EnrollInfo.objects.get(nrl_id=pk)
        serializer = EnrollSerializer(instance=enroll, data=request.data)
        res = {}

        if serializer.is_valid():
            serializer.save()
            res['status'] = 'Success'
            res['message'] = 'Update successful'
            return Response(res)
        else:
            return Response(serializer.errors)

@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def updatefaculty(request):

    if request.method == 'POST':
        pk = request.data['fct_id']
        faculty = FacultyInfo.objects.get(fct_id=pk)
        serializer = FactulySerializer  (instance=faculty, data=request.data)
        res = {}

        if serializer.is_valid():
            serializer.save()
            res['status'] = 'Success'
            res['message'] = 'Update successful'
            return Response(res)
        else:
            return Response(serializer.errors)

@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def updatedept(request):

    if request.method == 'POST':
        pk = request.data['dpt_id']
        faculty = DepartmentInfo.objects.get(dpt_id=pk)
        serializer = DepartmentSerializer  (instance=faculty, data=request.data)
        res = {}

        if serializer.is_valid():
            serializer.save()
            res['status'] = 'Success'
            res['message'] = 'Update successful'
            return Response(res)
        else:
            return Response(serializer.errors)

@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def updatesubject(request):

    if request.method == 'POST':
        pk = request.data['sub_id']
        faculty = SubjectInfo.objects.get(sub_id=pk)
        serializer = SubjectSerializer  (instance=faculty, data=request.data)
        res = {}

        if serializer.is_valid():
            serializer.save()
            res['status'] = 'Success'
            res['message'] = 'Update successful'
            return Response(res)
        else:
            return Response(serializer.errors)

@api_view(['DELETE']) # Update is_active instead of delete
@permission_classes([IsAuthenticated])
def deleteenroll(request, pk):
	enroll = EnrollInfo.objects.get(nrl_id=pk)
	enroll.delete()

	return Response('Delete successful!')