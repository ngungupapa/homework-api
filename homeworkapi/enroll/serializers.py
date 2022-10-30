from rest_framework import serializers
from .models import *

class FactulySerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyInfo
        fields ='__all__'
        # fields = ['fct_id', 'fct_name', 'fct_entry_date', 'fct_active']

class DepartmentSerializer(serializers.ModelSerializer):
    # faculty = serializers.CharField(source='dpt_faculty.fct_name')
    class Meta:
        model = DepartmentInfo
        fields ='__all__'
        # fields = ['dpt_id', 'dpt_name', 'dpt_entry_date', 'dpt_active', 'faculty']

class SubjectSerializer(serializers.ModelSerializer):
    # department = serializers.CharField(source='sub_department.dpt_name')
    class Meta:
        model = SubjectInfo
        fields ='__all__'
        # fields = ['sub_id', 'sub_name', 'sub_unit', 'sub_seat', 'sub_schedule', 'sub_active', 'department']

class EnrollSerializer(serializers.ModelSerializer):
    # student = serializers.CharField(source='nrl_student.fname')
    # subject = serializers.CharField(source='nrl_subject.sub_name')
    # schedule = serializers.CharField(source='nrl_subject.sub_schedule')
    class Meta:
        model = EnrollInfo
        fields ='__all__'
        # fields = ['nrl_id', 'student', 'subject', 'nrl_status', 'schedule', 'nrl_entry_date', 'nrl_lastmodify_date', 'nrl_active']

# class AddEnrollSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = EnrollInfo
#         fields ='__all__'

# class AddFacultySerializer(serializers.ModelSerializer):

#     class Meta:
#         model = FacultyInfo
#         fields ='__all__'

# class AddSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = FacultyInfo
#         fields ='__all__'