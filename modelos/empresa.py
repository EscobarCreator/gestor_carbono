"""Clase Empresa: contiene departamentos y suma sus emisiones.

Responsable: Miguel
Sprint: 2
"""

from modelos.departamento import Departamento


class Empresa:
    def __init__(self, nombre, rfc=None):
        # El nombre tiene que ser texto y no puede estar vacío
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("La empresa necesita un nombre")

        # El RFC es opcional, pero si se da debe tener 12 o 13 caracteres
        if rfc is not None:
            rfc = str(rfc).strip().upper()
            if len(rfc) != 12 and len(rfc) != 13:
                raise ValueError("El RFC debe tener 12 o 13 caracteres")

        self._nombre = nombre.strip()
        self._rfc = rfc
        self._departamentos = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def rfc(self):
        return self._rfc

    @property
    def departamentos(self):
        # Regresa una copia para que la lista no se cambie desde afuera
        return list(self._departamentos)

    def agregar_departamento(self, departamento):
        if not isinstance(departamento, Departamento):
            raise TypeError("Debe ser una instancia de Departamento")

        if self.buscar_departamento(departamento.nombre) is not None:
            raise ValueError("Ya existe un departamento con ese nombre")

        self._departamentos.append(departamento)

    def buscar_departamento(self, nombre):
        for departamento in self._departamentos:
            if departamento.nombre.lower() == nombre.lower():
                return departamento

        return None

    def calcular_emisiones_total(self):
        total = 0

        for departamento in self._departamentos:
            total += departamento.calcular_emisiones()

        return total

