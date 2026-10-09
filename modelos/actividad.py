"""Clase abstracta Actividad y sus hijas: ConsumoEnergetico, Transporte y Residuo.

Responsable: Ian
Sprint: 1
"""
from abc import ABC, abstractmethod


class Actividad(ABC):
    """Actividad corporativa que genera emisiones de CO2e (clase abstracta)."""

    def __init__(self, descripcion, cantidad):
        if not descripcion or not str(descripcion).strip():
            raise ValueError("La actividad necesita una descripción")
        if not isinstance(cantidad, (int, float)) or cantidad < 0:
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

    FACTOR_KG_POR_KWH = 0.44  # aproximado, red eléctrica de México

    def __init__(self, descripcion, kwh):
        super().__init__(descripcion, kwh)

    def calcular_emisiones(self):
        return self._cantidad * self.FACTOR_KG_POR_KWH


class Transporte(Actividad):
    """Combustible consumido por vehículos, medido en litros."""

    FACTORES = {"gasolina": 2.3, "diesel": 2.7}  # kg CO2e por litro, aproximados

    def __init__(self, descripcion, litros, tipo):
        super().__init__(descripcion, litros)
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

    FACTORES = {"relleno": 0.5, "reciclaje": 0.05}  # kg CO2e por kg, aproximados

    def __init__(self, descripcion, kg, tipo):
        super().__init__(descripcion, kg)
        if tipo not in self.FACTORES:
            raise ValueError(f"Tipo de residuo no válido: {tipo}")
        self._tipo = tipo

    @property
    def tipo(self):
        return self._tipo

    def calcular_emisiones(self):
        return self._cantidad * self.FACTORES[self._tipo]
