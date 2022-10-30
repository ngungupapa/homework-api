from django.contrib import admin
from .models import FacultyInfo, DepartmentInfo, SubjectInfo, EnrollInfo

# Register your models here.
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('fct_id','fct_name','fct_entry_date', 'fct_lastmodify_date', 'fct_active')
    readonly_fields=('fct_entry_date', 'fct_lastmodify_date')
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dpt_id','dpt_name','dpt_entry_date', 'dpt_entry_date', 'dpt_lastmodify_date', 'dpt_active', 'fct_name')
    readonly_fields=('dpt_entry_date', 'dpt_lastmodify_date')
    
    def fct_name(self, obj):
        return obj.dpt_faculty.fct_name

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('sub_id','sub_name','sub_unit', 'sub_seat', 'sub_schedule', 'sub_entry_date', 'sub_lastmodify_date', 'sub_active', 'sub_department')
    readonly_fields=('sub_entry_date', 'sub_lastmodify_date')
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class EnrollAdmin(admin.ModelAdmin):
    list_display = ('nrl_id','std_name','sub_name', 'nrl_status', 'nrl_entry_date', 'nrl_lastmodify_date', 'nrl_active')
    readonly_fields=('nrl_entry_date', 'nrl_lastmodify_date')
    
    def std_name(self, obj):
        return obj.nrl_student.fname
    def sub_name(self, obj):
        return obj.nrl_subject.sub_name

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(FacultyInfo, FacultyAdmin)
admin.site.register(DepartmentInfo, DepartmentAdmin)
admin.site.register(SubjectInfo, SubjectAdmin)
admin.site.register(EnrollInfo, EnrollAdmin)