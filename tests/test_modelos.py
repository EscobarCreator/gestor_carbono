"""Pruebas de las clases del modelo (Pytest).

Responsable: Juan Carlos
Sprint: 1
"""

import pytest       #Herramienta para hacer pruebas automáticas
from modelos.departamento import Departamento       #Clase de Miguel (por probarse) 

#Prueba 1: Crear un departamento con su nombre
def test_departamento_guarda_nombre():  
    assert Departamento("Ventas").nombre == "Ventas"

#Prueba 2: Si el nombre del departamento está vacío, la clase lo rechazará con un "ValueError"
def test_departamento_sin_nombre_falla():
    with pytest.raises(ValueError):     #Lanza el error por departamento sin nombre
        Departamento("")
