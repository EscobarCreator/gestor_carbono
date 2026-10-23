"""Clase Departamento: contiene actividades y suma sus emisiones.

Responsable: Miguel
Sprint: 2
"""

from modelos.actividad import Actividad


class Departamento:
    def __init__(self, nombre):
        # El nombre tiene que ser texto y no puede estar vacío
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El departamento necesita un nombre")

        self._nombre = nombre.strip()
        self._actividades = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def actividades(self):
        # Regresa una copia para que la lista no se cambie desde afuera
        return list(self._actividades)

    def agregar_actividad(self, actividad):
        if not isinstance(actividad, Actividad):
            raise TypeError("La actividad debe ser una instancia de Actividad")

        self._actividades.append(actividad)

    def calcular_emisiones(self):
        total = 0

        for actividad in self._actividades:
            total += actividad.calcular_emisiones()

        return total

