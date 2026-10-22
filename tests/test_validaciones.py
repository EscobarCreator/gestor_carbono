# Pruebas de validaciones de los modelos (Sprint 2)
# Responsable: Juan Carlos
# Cada prueba muestra un hueco encontrado al revisar los modelos.
# Van a fallar hasta que Miguel e Ian corrijan sus archivos.

import pytest
from modelos.empresa import Empresa
from modelos.departamento import Departamento
from modelos.actividad import ConsumoEnergetico, Transporte, Residuo


# Hueco 1: el tipo debe aceptarse aunque tenga mayusculas o espacios
def test_transporte_acepta_tipo_con_mayusculas():
    reparto = Transporte("Reparto", 10, "Gasolina")
    resultado_esperado = 10 * Transporte.FACTORES["gasolina"]
    assert reparto.calcular_emisiones() == pytest.approx(resultado_esperado)


def test_residuo_acepta_tipo_con_espacios():
    carton = Residuo("Carton", 20, " reciclaje ")
    resultado_esperado = 20 * Residuo.FACTORES["reciclaje"]
    assert carton.calcular_emisiones() == pytest.approx(resultado_esperado)


# Hueco 2: True no es una cantidad valida
def test_cantidad_true_falla():
    with pytest.raises(ValueError):
        ConsumoEnergetico("Luz oficina", True)


# Hueco 3: el nombre del departamento debe ser texto
def test_departamento_nombre_numero_falla():
    with pytest.raises(ValueError):
        Departamento(123)


# Hueco 4: la lista de actividades no se debe poder cambiar desde afuera
def test_actividades_no_se_modifican_desde_afuera():
    ventas = Departamento("Ventas")
    ventas.actividades.append("hola")
    assert len(ventas.actividades) == 0


# Hueco 5: el nombre de la empresa debe ser texto
def test_empresa_nombre_numero_falla():
    with pytest.raises(ValueError):
        Empresa(123)


# Hueco 6: la lista de departamentos no se debe poder cambiar desde afuera
def test_departamentos_no_se_modifican_desde_afuera():
    empresa = Empresa("EcoMex")
    empresa.departamentos.append("hola")
    assert len(empresa.departamentos) == 0


# Hueco 7: si se da un RFC, debe tener 12 o 13 caracteres
def test_rfc_invalido_falla():
    with pytest.raises(ValueError):
        Empresa("EcoMex", "x")


def test_rfc_valido_se_guarda():
    empresa = Empresa("EcoMex", "ABC123456XYZ")
    assert empresa.rfc == "ABC123456XYZ"
