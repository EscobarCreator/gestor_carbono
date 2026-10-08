"""
Pruebas de las clases del modelo (Pytest).
Responsable: J. Carlos
Sprint: 1
"""

import pytest       #Herramienta para hacer pruebas automáticas
from modelos.empresa import Empresa         #Clase de Miguel (por probarse)
from modelos.departamento import Departamento       #Clase de Miguel (por probarse) 
from modelos.actividad import Actividad, ConsumoEnergetico, Transporte, Residuo    #Clase de Ian (por probarse)

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
    assert Empresa("EcoMex S.A.").nombre == "EcoMex S.A." #Corroborar con Miguel si ".nombre" es con "." o "_"
    
#Prueba 5: Error al agregar 2 departamentos con el mismo nombre
def test_empresa_no_repite_departamento():
    empresa = Empresa("EcoMex S.A.")
    empresa.agregar_departamento(Departamento("Ventas"))
    with pytest.raises(ValueError): 
        empresa.agregar_departamento(Departamento("Ventas"))

#Prueba 6: Contar emisiones al agregar un departamento con actividad de consumo energético
def test_departamento_guarda_actividades():
    ventas = Departamento("Ventas")
    ventas.agregar_actividad(ConsumoEnergetico("Luz", 100))
    assert ventas.calcular_emisiones() == pytest.approx(44)

#Prueba 7: Validar que sean únicamente números positivos los consumos energéticos
def test_cantidad_negativa_falla():
    with pytest.raises(ValueError): 
        ConsumoEnergetico("Luz", -5)

#Prueba 8: Validar que "actividad" corresponda a "luz, transporte o residuo"
def test_actividad_directa_falla():
    with pytest.raises(TypeError): 
        Actividad("x", 1)

#Prueba 9: 50L de gasolina x 2.31 debe dar 115kg de Co2
def test_transporte_calcula():
    t = Transporte("Reparto", 50, "gasolina")
    assert t.calcular_emisiones() == pytest.approx(115)

#Prueba 10: 200kg de residuo x 0.5 = 100kg de Co2
def test_residuo_calcula():
    r = Residuo("Basura", 200, "relleno")
    assert r.calcular_emisiones() == pytest.approx(100)




