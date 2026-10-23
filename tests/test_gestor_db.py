# Pruebas de la base de datos GestorDB (Sprint 2)
# Responsable: Juan Carlos
# tmp_path es una carpeta temporal que da pytest, así la base de prueba
# no se guarda en el proyecto.

import pytest
from modelos.empresa import Empresa
from modelos.departamento import Departamento
from modelos.actividad import ConsumoEnergetico, Transporte, Residuo
from datos.gestor_db import GestorDB


# Función de apoyo: arma una empresa de ejemplo con 2 departamentos
def crear_empresa_ejemplo():
    empresa = Empresa("EcoMex")

    ventas = Departamento("Ventas")
    ventas.agregar_actividad(ConsumoEnergetico("Luz oficina", 100))
    ventas.agregar_actividad(Transporte("Reparto", 50, "gasolina"))

    almacen = Departamento("Almacen")
    almacen.agregar_actividad(Residuo("Carton", 200, "relleno"))

    empresa.agregar_departamento(ventas)
    empresa.agregar_departamento(almacen)
    return empresa


# Guardar, cerrar y volver a cargar debe dar el mismo total
def test_guardar_y_cargar_mismo_total(tmp_path):
    ruta = tmp_path / "prueba.db"
    original = crear_empresa_ejemplo()

    db = GestorDB(ruta)
    db.guardar_empresa(original)
    db.cerrar()

    db = GestorDB(ruta)
    cargada = db.cargar_empresa("EcoMex")
    db.cerrar()

    assert cargada.calcular_emisiones_total() == pytest.approx(original.calcular_emisiones_total())


# Al cargar deben regresar los mismos departamentos
def test_cargar_recupera_departamentos(tmp_path):
    db = GestorDB(tmp_path / "prueba.db")
    db.guardar_empresa(crear_empresa_ejemplo())
    cargada = db.cargar_empresa("EcoMex")
    db.cerrar()

    assert len(cargada.departamentos) == 2
    assert cargada.buscar_departamento("Almacen") is not None


# Guardar dos veces no debe duplicar las actividades
def test_guardar_dos_veces_no_duplica(tmp_path):
    db = GestorDB(tmp_path / "prueba.db")
    empresa = crear_empresa_ejemplo()
    db.guardar_empresa(empresa)
    db.guardar_empresa(empresa)
    cargada = db.cargar_empresa("EcoMex")
    db.cerrar()

    ventas = cargada.buscar_departamento("Ventas")
    assert len(ventas.actividades) == 2


# Cargar una empresa que no se guardó regresa una empresa sin departamentos
def test_cargar_empresa_que_no_existe(tmp_path):
    db = GestorDB(tmp_path / "prueba.db")
    cargada = db.cargar_empresa("NoExiste")
    db.cerrar()

    assert len(cargada.departamentos) == 0
