"""CalculadoraHuella: emisiones por departamento, por tipo y total.

Responsable: Miguel
Sprint: 2
"""


class CalculadoraHuella:
    """Calcula la huella de una empresa por departamento, por tipo y total."""

    def __init__(self, empresa):
        self._empresa = empresa

    def total(self):
        return self._empresa.calcular_emisiones_total()

    def por_departamento(self):
        resultado = {}
        for depto in self._empresa.departamentos:
            resultado[depto.nombre] = depto.calcular_emisiones()
        return resultado

    def por_tipo(self):
        resultado = {"ConsumoEnergetico": 0, "Transporte": 0, "Residuo": 0}
        for depto in self._empresa.departamentos:
            for actividad in depto.actividades:
                resultado[type(actividad).__name__] += actividad.calcular_emisiones()
        return resultado

    def departamento_mayor(self):
        mayor = None
        for depto in self._empresa.departamentos:
            if mayor is None or depto.calcular_emisiones() > mayor.calcular_emisiones():
                mayor = depto
        return mayor

