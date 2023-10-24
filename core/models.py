from django.db import models

# Create your models here.

class Empleado(models.Model):
    id_empleado=models.AutoField(primary_key=True)
    rut_empleado=models.CharField(max_length=10)
    nombre_emp=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    cargo=models.CharField(max_length=10)
    salario=models.CharField(max_length=6)
   
    def __str__(self):
       return self.nombre_emp 
   

class Vehiculo (models.Model): 
    id_vehi= models.AutoField(primary_key=True)
    patente=models.CharField(max_length=6)
    modelo=models.CharField(max_length=10)
    marca=models.CharField(max_length=10)
    año=models.CharField(max_length=10)
    version=models.CharField(max_length=10)
    
    def __str__(self):
        return self.patente
    
class  Cliente(models.Model):
    id_cli=models.AutoField(primary_key=True)
    rut_cli=models.CharField(max_length=10)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    telefono=models.CharField(max_length=9)
    email=models.CharField(max_length=30)
    patente=models.ForeignKey(Vehiculo,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre    

class Proveedor(models.Model):
    id_proveedor=models.AutoField(primary_key=True)
    nombre_prov=models.CharField(max_length=30)
    producto=models.CharField(max_length=20) 
    telefono=models.CharField(max_length=9)
    direccion=models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre_prov 
    
class Pedido (models.Model):
    id_pedido=models.AutoField(primary_key=True)
    estado=models.CharField(max_length=10)
    producto=models.CharField(max_length=20)
    nombre_emp=models.ForeignKey(Empleado, on_delete=models.CASCADE)
    nombre_prov=models.ForeignKey(Proveedor, on_delete=models.CASCADE)
        
    def __str__(self):
        return self.producto
    
class Servicio (models.Model):
    id_servicio=models.AutoField(primary_key=True)
    tipo_servicio=models.CharField(max_length=30)
    precio=models.CharField(max_length=6)
    patente=models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    nombre_emp=models.ForeignKey(Empleado, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.tipo_servicio
    
class Factura (models.Model):
    id_factura=models.AutoField(primary_key=True)
    fecha=models.DateTimeField()   
    rut_cli=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo_servicio=models.ForeignKey(Servicio, on_delete=models.CASCADE)
    nombre_emp=models.ForeignKey(Empleado, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.fecha
    