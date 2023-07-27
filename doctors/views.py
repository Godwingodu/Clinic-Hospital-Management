import pandas as pd

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View,CreateView,FormView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

from .forms import Logform,Regform,User
from patients.models import Patients


#Front-page view
class FrontView(View):
    def get(self,request):
        return render(request,"frontpage.html")
    

#Home-page view
class HomeView(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            patients = Patients.objects.all()
            url = request.META.get('HTTP_REFERER') #get the referring URL
            if 'end_index = 15' in url:
                items_per_page = int(request.GET.get('end_index',15))
            elif 'end_index = 10' in url:
                items_per_page = int(request.GET.get('end_index',10))
            else:
                items_per_page = int(request.GET.get('end_index',5))
            paginator = Paginator(patients, items_per_page)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request,"homepage.html",{"patients":page_obj})
        else:
            return redirect("login")
        
        
#Registration-page view         
class RegistrationView(CreateView):
    template_name = "registration.html"
    form_class = Regform
    model = User
    success_url = reverse_lazy('login')
    def form_valid(self,form):
        self.object = form.save()
        messages.success(self.request,"Registration Succesfull")
        return super().form_valid(form)
    
    
#Login-page view
class LoginView(FormView):
    template_name = "login.html"
    form_class = Logform
    def post(self,request,*args,**kwargs):
        form_data = Logform(data = request.POST)
        if form_data.is_valid():
            un = form_data.cleaned_data.get("username")
            pw = form_data.cleaned_data.get("password")
            user = authenticate(request,username = un,password = pw)
            if user:
                login(request,user)
                return redirect("homepage")
            else:
                messages.error(request,"Enter correct details")
                return redirect("login")
        else:
            return render(request,"login.html",{"form":form_data})
        

#Logout View
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('frontpage')
    

#Export data to pdf format
def export_to_pdf(request):
    data = Patients.objects.all() 
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Patients_data.pdf"'
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []
    data_list = [['Full Name','Dob','Gender','Contact Number','Address','Medical Condition'],] 
    for item in data:
        data_list.append([item.fullname, item.dob, item.gender,item.contact_number,item.address,item.medical_condition]) 
    table = Table(data_list)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), 'gray'),
        ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), 'lightgrey'),
    ]))
    elements.append(table)
    doc.build(elements)
    return response


#Export data to Excel format
def export_to_excel(request): 
    data = Patients.objects.all()  
    data_list = [['Full Name','Dob','Gender','Contact Number','Address','Medical Condition'],] 
    for item in data:
        data_list.append([item.fullname, item.dob, item.gender,item.contact_number,item.address,item.medical_condition])     
    df = pd.DataFrame(data_list)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Patients_data.xlsx"'
    df.to_excel(response, index=False)
    return response


#Export data to Csv format
def export_to_csv(request):
    data = Patients.objects.all()  
    data_list = [['Full Name','Dob','Gender','Contact Number','Address','Medical Condition'],] 
    for item in data:
        data_list.append([item.fullname, item.dob, item.gender,item.contact_number,item.address,item.medical_condition]) 
    df = pd.DataFrame(data_list)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Patients_data.csv"'
    df.to_csv(response, index=False)
    return response