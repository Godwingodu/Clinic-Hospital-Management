from django.urls import path
from . import views

urlpatterns = [
    path('',views.FrontView.as_view(),name="frontpage"),
    path('registration/',views.RegistrationView.as_view(),name="reg"),
    path('login/',views.LoginView.as_view(),name="login"),
    path('logout/',views.LogoutView.as_view(),name="logout"),
    path('homepage/',views.HomeView.as_view(),name="homepage"),
    path('exporttopdf/',views.export_to_pdf,name="exporttopdf"),
    path('exporttoexcel/',views.export_to_excel,name="exporttoexcel"),
    path('exporttocsv/',views.export_to_csv,name="exporttocsv")
]