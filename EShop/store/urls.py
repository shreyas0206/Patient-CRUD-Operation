from django.contrib import admin
from django.urls import path
from . import views
from .views import *
from django.contrib.auth.views import LogoutView,PasswordChangeView,PasswordChangeDoneView

urlpatterns = [
    path('',views.index),
    path('AllProduct/',AllProduct.as_view(),name='All_Product'),
    path('signup/',SignUpView.as_view(),name='signup'),
    path('cart/',Cart.as_view(),name='cart'),
    path('checkout/',CheckOut.as_view(),name='checkout'),
    path('your-order/',YourOrders.as_view(),name='your_order'),
    path('update/<int:pk>',UpdateUserView.as_view(),name='update'),
    path('login/',LogInView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='/login/'),name='logout'),
    path('change-password/<int:pk>',PasswordChangeView.as_view(template_name='change_password.html'),name='change-password'),
    path('password-change-done/',PasswordChangeDoneView.as_view(template_name='password_changed.html'),name='password_change_done'),

]

