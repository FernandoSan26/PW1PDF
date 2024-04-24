from django.urls import path
from . import views

urlpatterns = [
    path('importar-pdf/', views.importar_pdf, name='importar_pdf'),
    path('import-success/', views.import_success, name='import_success'),
    path('Select-pdf/', views.filtrar_materias, name='filtrar_materias'),
    path('mostrar-pdf/',views.mostrar_pdf,name='mostrar_pdf'),

]
