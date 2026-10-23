# Pruebas de CalculadoraHuella (Sprint 2)
# Responsable: Juan Carlos
# Los resultados esperados se sacan de los mismos modelos,
# así las pruebas siguen sirviendo aunque cambien los factores.

import pytest
from modelos.empresa import Empresa
from modelos.departamento import Departamento
from modelos.actividad import ConsumoEnergetico, Transporte, Residuo
from servicios.calculadora_huella import CalculadoraHuella


# Función de apoyo: Almacen emite más que Ventas a propósito
def crear_empresa_ejemplo():
    empresa = Empresa("EcoMex")

    ventas = Departamento("Ventas")
    ventas.agregar_actividad(ConsumoEnergetico("Luz oficina", 100))
    ventas.agregar_actividad(Transporte("Reparto", 50, "gasolina"))

    almacen = Departamento("Almacen")
    almacen.agregar_actividad(Residuo("Carton", 1000, "relleno"))

    empresa.agregar_departamento(ventas)
    empresa.agregar_departamento(almacen)
    return empresa


# El total de la calculadora debe ser igual al de la empresa
def test_total():
    empresa = crear_empresa_ejemplo()
    calculadora = CalculadoraHuella(empresa)
    assert calculadora.total() == pytest.approx(empresa.calcular_emisiones_total())


# Debe regresar el total de cada departamento
def test_por_departamento():
    empresa = crear_empresa_ejemplo()
    calculadora = CalculadoraHuella(empresa)
    resultado = calculadora.por_departamento()

    ventas = empresa.buscar_departamento("Ventas")
    assert len(resultado) == 2
    assert resultado["Ventas"] == pytest.approx(ventas.calcular_emisiones())


# La suma por tipo debe dar el total, y la luz debe estar en ConsumoEnergetico
def test_por_tipo():
    empresa = crear_empresa_ejemplo()
    calculadora = CalculadoraHuella(empresa)
    resultado = calculadora.por_tipo()

    luz = ConsumoEnergetico("Luz oficina", 100)
    suma = resultado["ConsumoEnergetico"] + resultado["Transporte"] + resultado["Residuo"]

    assert resultado["ConsumoEnergetico"] == pytest.approx(luz.calcular_emisiones())
    assert suma == pytest.approx(calculadora.total())


# El departamento que más emite debe ser Almacen
def test_departamento_mayor():
    calculadora = CalculadoraHuella(crear_empresa_ejemplo())
    mayor = calculadora.departamento_mayor()
    assert mayor.nombre == "Almacen"


# Una empresa sin departamentos da total 0 y no tiene departamento mayor
def test_empresa_vacia():
    calculadora = CalculadoraHuella(Empresa("Vacia"))
    assert calculadora.total() == 0
    assert calculadora.departamento_mayor() is None