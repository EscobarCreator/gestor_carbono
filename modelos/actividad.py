"""Clase abstracta Actividad y sus hijas: ConsumoEnergetico, Transporte y Residuo.

Responsable: Ian
Sprint: 2
"""
from abc import ABC, abstractmethod


class Actividad(ABC):
    """Actividad corporativa que genera emisiones de CO2e (clase abstracta)."""

    def __init__(self, descripcion, cantidad):
        if not descripcion or not str(descripcion).strip():
            raise ValueError("La actividad necesita una descripción")
        # True y False no cuentan como cantidad (en Python True vale 1)
        if isinstance(cantidad, bool) or not isinstance(cantidad, (int, float)) or cantidad < 0:
            raise ValueError("La cantidad debe ser un número positivo")
        self._descripcion = str(descripcion).strip()
        self._cantidad = cantidad

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def cantidad(self):
        return self._cantidad

    @abstractmethod
    def calcular_emisiones(self):
        """Regresa las emisiones en kg de CO2e. Cada hija lo implementa."""

    def __str__(self):
        return f"{type(self).__name__}: {self._descripcion} ({self.calcular_emisiones():.1f} kg CO2e)"


class ConsumoEnergetico(Actividad):
    """Consumo de electricidad medido en kWh."""

    FACTOR_KG_POR_KWH = 0.444  # SEMARNAT, factor del SEN 2024

    def __init__(self, descripcion, kwh):
        super().__init__(descripcion, kwh)

    def calcular_emisiones(self):
        return self._cantidad * self.FACTOR_KG_POR_KWH


class Transporte(Actividad):
    """Combustible consumido por vehículos, medido en litros."""

    FACTORES = {"gasolina": 2.32, "diesel": 2.70}  # kg CO2e por litro, EPA 2025, Tabla 2

    def __init__(self, descripcion, litros, tipo):
        super().__init__(descripcion, litros)
        # Se limpia el tipo: " Gasolina " queda como "gasolina"
        tipo = str(tipo).strip().lower()
        if tipo not in self.FACTORES:
            raise ValueError(f"Tipo de combustible no válido: {tipo}")
        self._tipo = tipo

    @property
    def tipo(self):
        return self._tipo

    def calcular_emisiones(self):
        return self._cantidad * self.FACTORES[self._tipo]


class Residuo(Actividad):
    """Residuos generados, medidos en kg."""

    FACTORES = {"relleno": 0.64, "reciclaje": 0.10}  # kg CO2e por kg, EPA 2025, Tabla 9

    def __init__(self, descripcion, kg, tipo):
        super().__init__(descripcion, kg)
        # Se limpia el tipo: " Gasolina " queda como "gasolina"
        tipo = str(tipo).strip().lower()
        if tipo not in self.FACTORES:
            raise ValueError(f"Tipo de residuo no válido: {tipo}")
        self._tipo = tipo

    @property
    def tipo(self):
        return self._tipo

    def calcular_emisiones(self):
        return self._cantidad * self.FACTORES[self._tipo]
