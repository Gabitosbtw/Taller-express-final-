from django.urls import path
from .views import inicio, inicio2, autos, motos, contacto, crearcuenta, login, reseñas, reserva, ford_mustang, volkswagen,lamboghini,guerrero,honda,yamaha,reserva_msj
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',inicio,name="inicio"),
    path('inicio2/',inicio2,name="inicio2"),
    path('autos/',autos,name="autos"),
    path('motos/',motos,name="motos"),
    path('contacto/',contacto,name="contacto"),
    path('crearcuenta/',crearcuenta,name="crearcuenta"),
    path('login/',login, name="login"),
    path('reseñas/',reseñas,name="reseñas"), 
    path('reserva/',reserva,name="reserva"),    
    path('reserva_msj/',reserva_msj,name="reserva_msj"),   
    path('ford_mustang/',ford_mustang,name="ford_mustang"), 
    path('volkswagen/',volkswagen,name="volkswagen"), 
    path('lamboghini/',lamboghini,name="lamboghini"), 
    path('guerrero/',guerrero,name="guerrero"), 
    path('honda/',honda,name="honda"), 
    path('yamaha/',yamaha,name="yamaha")
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
