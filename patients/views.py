from django.shortcuts import render,redirect
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.db.models import Q

from .models import Patients
from .forms import PatientsForm


#decorator
def signin_required(func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return func(request,*args,**kwargs)
        else:
            return redirect('login')
    return wrapper  


#Add patient View
@method_decorator(signin_required,name = 'dispatch')
class AddPatient(CreateView):
    template_name = "addpatients.html"
    form_class = PatientsForm
    model = Patients
    success_url = reverse_lazy('homepage')
    def form_valid(self,form) :
        self.object = form.save()
        messages.success(self.request,"patient added succesfully")
        return super().form_valid(form)
    

#Edit patient view
@method_decorator(signin_required,name='dispatch')
class EditPatient(UpdateView):
    template_name="editpatient.html"
    form_class = PatientsForm
    model = Patients
    success_url = reverse_lazy('homepage')
    pk_url_kwarg = "pk"
    def form_valid(self,form):
        self.object = form.save()
        messages.info(self.request,"Patient Details Updated")
        return super().form_valid(form)


#Delete patient View
@method_decorator(signin_required,name = 'dispatch')
class DeletePatientView(DeleteView):
    template_name = "deletepatient.html"
    model = Patients
    success_url = reverse_lazy('homepage')
    def form_valid(self,form) :
        messages.warning(self.request,"patient Deleted succesfully")
        return super().form_valid(form)
    
    
#Specific patient view
@method_decorator(signin_required,name='dispatch')
class SpecificPatientView(DetailView):
    template_name="specificpatient.html"
    model = Patients


#Search View
def search(request): 
    if request.method == 'GET':      
        searchinput =  request.GET.get('search') or '' 
        if searchinput:
            patients = Patients.objects.filter(Q(fullname__icontains = searchinput)|Q(medical_condition__icontains = searchinput)) 
            return render(request,"homepage.html",{"searchinput":searchinput,'patients':patients})
        else:
            patients = Patients.objects.all()
            return render(request,"homepage.html",{"searchinput":searchinput,'patients':patients})


