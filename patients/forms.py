from django import forms
from django.utils.timezone import now

from .models import Patients

#Patients form
class PatientsForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = ["fullname","dob","gender","contact_number","address","medical_condition","profile_pic"]
        widgets = {
            "fullname":forms.TextInput(attrs = {"class":"form-control","placeholder":"Enter the Fullname"}),
            "dob":forms.DateInput(attrs = {'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}),
            "gender":forms.Select(attrs={"class":"form-control"}),
            "contact_number":forms.NumberInput(attrs = {"class":"form-control","placeholder":"Enter the Contact number"}),
            "address":forms.Textarea(attrs = {"class":"form-control"}),
            "medical_condition":forms.Textarea(attrs = {"class":"form-control"}),
            "profle_pic":forms.FileInput(),
        }
    #form validation
    def clean(self):
        cleaned_data = super().clean()

        fullname = cleaned_data.get('fullname')
        dob = cleaned_data.get('dob')
        contact_number = cleaned_data.get('contact_number')
        address = cleaned_data.get('address')
        medical_condition = cleaned_data.get('medical_condition')

        if not fullname or len(fullname.strip()) < 3:
            self.add_error('fullname', 'Fullname must be at least 3 characters long.')

        if not dob or dob > now().date():
            self.add_error('dob', 'Please provide a valid date of birth.')

        if not contact_number or len(str(contact_number)) != 10:
            self.add_error('contact_number', 'Contact number must be exactly 10 digits.')

        if not address or len(address.strip()) < 20:
            self.add_error('address', 'Address must be at least 20 characters long.')
            
        if not medical_condition or len(medical_condition.strip()) < 20:
            self.add_error('medical_condition', 'Medical Condition must be at least 20 characters long.')
            
        return cleaned_data
