from django.test import TestCase, Client
from patients.models import Patients
from patients.views import *
from django.urls import reverse


# Create your tests here.
class PatientTestCase(TestCase):
    def test_create_model(self):
        Patients.objects.create(fullname='Godwin vinson', dob='1999-12-12',contact_number='7025190151',address='Chalakkal House Pulikkakadavu Road p.o kundaliyur Thrissur',medical_condition='Chalakkal House Pulikkakadavu Road p.o kundaliyur Thrissur')
     
    # Test that the view returns the expected HTTP response status code (200 for success)
    def test_view_response(self):
            url = reverse(search)  
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            
    def setUp(self):
            self.client = Client()
            self.add_patient_url = reverse('addpatient') 
            self.edit_patient_url = reverse('editpatient', kwargs={'pk': 1})  
            self.delete_patient_url = reverse('deletepatient', kwargs={'pk': 1})
            self.specific_patient_url = reverse('specificpatient', kwargs={'pk': 1})  
            
