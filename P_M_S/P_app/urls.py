from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('AllPatient/',AllPatient,name='All_Patient'),
    # path('AddPatient/',AddPatient,name='AddPatient'),
    # path('post/',post),
    path('AddPatient/',AddPatientView.as_view(),name='AddPatient'),
    path('DeletePatient/<int:pk>',DeletePatientView.as_view(),name='DeletePatient'),
    path('UpdatePatient/<int:pk>',UpdatePatientView.as_view(),name='UpdatePatient'),
    path('AdminLogin/',LogInView.as_view(),name='AdminLogin'),
    path('Adminlogout/',LogoutView.as_view(next_page='/AdminLogin/'),name='Adminlogout'),


]
