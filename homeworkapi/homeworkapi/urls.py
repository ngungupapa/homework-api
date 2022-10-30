"""homeworkapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from account.views import *
from enroll.views import *
from enroll.views_enroll import *

router = DefaultRouter()
router.register(r'faculty', FacultyViewSet)
router.register(r'department', DepartmentViewSet)
router.register(r'subject', SubjectViewSet)
router.register(r'enrollinfo', EnrollViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    # path('api-token-auth/', views.obtain_auth_token),
    # Account
    path('register/', registration_view),
    path('login/', Login_view),
    path('logout/', Logout_view),
    path('changepassword/', chgpass_view),
    # Enroll
    path('addenroll/', addenroll),
    path('addfaculty/', addfaculty),
    path('adddept/', adddept),
    path('addsubject/', addsubject),

    path('updateenroll/', updateenroll),
    path('updatefaculty/', updatefaculty),
    path('updatedept/', updatedept),
    path('updatesubject/', updatesubject),

    path('deleteenroll/<str:pk>/', deleteenroll),
]
