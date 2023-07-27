from django.urls import path
from . import views

urlpatterns = [
    path('addpatient/',views.AddPatient.as_view(),name = "addpatient"),
    path('editpatient/<int:pk>',views.EditPatient.as_view(),name = "editpatient"),
    path('deletepatient/<int:pk>',views.DeletePatientView.as_view(),name = "deletepatient"),
    path('specificpatient/<int:pk>',views.SpecificPatientView.as_view(),name = "specificpatient"),
    path('search/',views.search, name = 'search')
]
