"""Pruebas de las clases del modelo (Pytest).

Responsable: Juan Carlos
Sprint: 1
"""

import pytest
from modelos.departamento import Departamento 

def test_departamento_guarda_nombre():
    assert Departamento("Ventas").nombre == "Ventas"

def test_departamento_sin_nombre_falla():
    with pytest.raises(ValueError):
        Departamento("")
