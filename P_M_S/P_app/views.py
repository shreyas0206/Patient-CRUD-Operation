from django.shortcuts import render,redirect
# from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth.views import LoginView,LogoutView
from .forms import AddPatientForm,LogInForm
from django.views.generic import View
from django.contrib.auth import authenticate,login

from .models import *

# Create your views here.
def home(request):
    return render(request,'index.html')
def AllPatient(request):
    data=Patient.objects.all()
    return render(request,'all.html',{'data':data})

# ---------- function base view ------------------------
# def AddPatient(request):
#         form = AddPatientForm()
#         return render(request,'add.html',{'form':form})
# def post(request):
#         form = AddPatientForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/AllPatient')
# ---------------------------------------------------------

# -------------- class base view --------------------------
# ---------------------------------------------------------
# # This is normal create view | form disign is low
# class AddPatientView(CreateView):
#     model = Patient
#     fields = '__all__'
#     template_name = 'add.html'
#     success_url = '/AllPatient/'
# ---------------------------------------------------------
class AddPatientView(CreateView):
    form_class = AddPatientForm #we add form in crateview
    template_name = 'add.html' 
    success_url = '/AllPatient/'
class DeletePatientView(DeleteView):
    model = Patient
    template_name = 'delete.html'
    success_url = '/AllPatient/'

class UpdatePatientView(UpdateView):
    model = Patient
    fields = '__all__'
    template_name = 'Update.html'
    success_url = '/AllPatient/'


# class AdminLoginView(LoginView):
#     form_class = LogInForm #we add form in crateview
#     template_name = 'login.html'
#     redirect_authenticated_user = True

class LogInView(View):
    def get(self,request):
        form = LogInForm()
        return render(request,'login.html',{'form':form})
    
    def post(self,request):
        form=LogInForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(username,password)
            # messages.success(request,f'Welcome {username}')
            user=authenticate(username=username,password=password)
            print(user)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                return render(request,'login.html',{'form':form})

        else:
            return render(request,'login.html',{'form':form})