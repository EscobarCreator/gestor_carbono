"""Punto de entrada del Gestor de Carbono Corporativo.

Responsable de integrar: Emmanuel (Scrum Master)
Demo del Sprint 1: Empresa, Departamento y Actividad.
"""
from modelos.empresa import Empresa
from modelos.departamento import Departamento
from modelos.actividad import ConsumoEnergetico, Transporte, Residuo


def main():
    empresa = Empresa("EcoMex S.A.")
    ventas = Departamento("Ventas")
    almacen = Departamento("Almacén")
    empresa.agregar_departamento(ventas)
    empresa.agregar_departamento(almacen)

    ventas.agregar_actividad(ConsumoEnergetico("Luz oficina", 1200))
    almacen.agregar_actividad(Transporte("Reparto", 300, "diesel"))
    almacen.agregar_actividad(Residuo("Cartón", 150, "relleno"))

    print(f"Gestor de Carbono Corporativo - {empresa.nombre}")
    print("-" * 45)
    for d in empresa.departamentos:
        print(f"{d.nombre}: {d.calcular_emisiones():.1f} kg CO2e")
        for a in d.actividades:
            print("   ", a)
    print("-" * 45)
    print(f"Total: {empresa.calcular_emisiones_total():.1f} kg CO2e")


if __name__ == "__main__":
    main()
