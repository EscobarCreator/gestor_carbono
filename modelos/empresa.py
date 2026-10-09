"""Clase Empresa: contiene departamentos y suma sus emisiones.

Responsable: Miguel
Sprint: 1
"""

from modelos.departamento import Departamento


class Empresa:
    def __init__(self, nombre, rfc=None):
        if not nombre or not nombre.strip():
            raise ValueError("La empresa necesita un nombre")

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
        return self._departamentos

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


if __name__ == "__main__":
    empresa = Empresa("Empresa Ejemplo", "ABC123456XYZ")

    ventas = Departamento("Ventas")
    empresa.agregar_departamento(ventas)

    print(empresa.nombre)
    print(empresa.buscar_departamento("Ventas").nombre)
    print(empresa.calcular_emisiones_total())
