"""
Pruebas de las clases del modelo (Pytest).
Responsable: J. Carlos
Sprint: 1
"""

import pytest       #Herramienta para hacer pruebas automáticas
from modelos.empresa import Empresa         #Clase de Miguel (por probarse)
from modelos.departamento import Departamento       #Clase de Miguel (por probarse) 
from modelos.actividad import ConsumoEnergetico     #Clase de Ian (por probarse)

#Prueba 1: Crear un departamento con su nombre
def test_departamento_guarda_nombre():  
    assert Departamento("Ventas").nombre == "Ventas"

#Prueba 2: Si el nombre del departamento está vacío, la clase lo rechazará con un "ValueError"
def test_departamento_sin_nombre_falla():
    with pytest.raises(ValueError):     #Lanza el error por departamento sin nombre
        Departamento("")

#Prueba 3: 100 kWh x 0.44 debe dar 44kg de Co2
def test_consumo_energetico_calcula():
    c = ConsumoEnergetico("Luz", 100)
    assert c.calcular_emisiones() == pytest.approx(44)

#Prueba 4: Se crea una empresa con nombre, guarda el nombre
def test_empresa_se_crea_con_nombre():
    assert Empresa("EcoMex S.A.").nombre == "EcoMex S.A." #Corroborar si "nombre" es con "." o "_"
    
#Prueba 5: Error al agregar 2 departamentos con el mismo nombre
def test_empresa_no_repite_departamento():
    empresa = Empresa("EcoMex S.A.")
    empresa.agregar_departamento(Departamento("Ventas"))
    with pytest.raises(ValueError): 
        empresa.agregar_departamento(Departamento("Ventas"))
        

