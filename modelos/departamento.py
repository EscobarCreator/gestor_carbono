"""Clase Departamento: contiene actividades y suma sus emisiones.

Responsable: Miguel
Sprint: 1
"""

from modelos.actividad import Actividad


class Departamento:
    def __init__(self, nombre):
        if not nombre or not nombre.strip():
            raise ValueError("El departamento necesita un nombre")

        self._nombre = nombre.strip()
        self._actividades = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def actividades(self):
        return self._actividades
      
    def agregar_actividad(self, actividad):
        if not isinstance(actividad, Actividad):
            raise TypeError("La actividad debe ser una instancia de Actividad")

        self._actividades.append(actividad)

    def calcular_emisiones(self):
        total = 0

        for actividad in self._actividades:
            total += actividad.calcular_emisiones()

        return total


if __name__ == "__main__":
    d = Departamento("Ventas")
    print(d.nombre)

    Departamento("")
