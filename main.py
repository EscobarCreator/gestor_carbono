"""Punto de entrada del Gestor de Carbono Corporativo.

Responsable de integrar: Emmanuel (Scrum Master)
Sprint: 2
Menú de consola: registrar actividades, ver la huella y guardar/cargar en SQLite.
"""
from modelos.empresa import Empresa
from modelos.departamento import Departamento
from modelos.actividad import ConsumoEnergetico, Transporte, Residuo
from servicios.calculadora_huella import CalculadoraHuella
from datos.gestor_db import GestorDB


def mostrar_menu():
    print()
    print("=" * 45)
    print("  GESTOR DE CARBONO CORPORATIVO")
    print("=" * 45)
    print("1) Agregar departamento")
    print("2) Registrar actividad")
    print("3) Ver huella por departamento y por tipo")
    print("4) Ver total y departamento con más emisiones")
    print("5) Guardar en la base de datos")
    print("6) Cargar de la base de datos")
    print("0) Salir")


def pedir_numero(mensaje):
    texto = input(mensaje)
    try:
        return float(texto)
    except ValueError:
        # float() da un error en inglés; lo cambiamos por uno en español
        raise ValueError("La cantidad debe ser un número")


def agregar_departamento(empresa):
    nombre = input("Nombre del departamento: ")
    empresa.agregar_departamento(Departamento(nombre))
    print("Departamento agregado.")


def registrar_actividad(empresa):
    if len(empresa.departamentos) == 0:
        print("Primero agrega un departamento (opción 1).")
        return

    nombre = input("Departamento: ")
    departamento = empresa.buscar_departamento(nombre)
    if departamento is None:
        raise ValueError("No existe un departamento con ese nombre")

    print("Clase de actividad: 1) Luz  2) Transporte  3) Residuo")
    clase = input("Elige una opción: ")
    descripcion = input("Descripción: ")

    if clase == "1":
        kwh = pedir_numero("Consumo en kWh: ")
        actividad = ConsumoEnergetico(descripcion, kwh)
    elif clase == "2":
        litros = pedir_numero("Litros de combustible: ")
        tipo = input("Combustible (gasolina / diesel): ")
        actividad = Transporte(descripcion, litros, tipo)
    elif clase == "3":
        kg = pedir_numero("Kilos de residuo: ")
        tipo = input("Destino (relleno / reciclaje): ")
        actividad = Residuo(descripcion, kg, tipo)
    else:
        raise ValueError("Clase no válida, elige 1, 2 o 3")

    departamento.agregar_actividad(actividad)
    print(f"Actividad registrada: {actividad.calcular_emisiones():.1f} kg CO2e")


def ver_huella(empresa):
    calculadora = CalculadoraHuella(empresa)

    print("\nHuella por departamento:")
    por_departamento = calculadora.por_departamento()
    if len(por_departamento) == 0:
        print("   (no hay departamentos)")
    for nombre in por_departamento:
        print(f"   {nombre}: {por_departamento[nombre]:.1f} kg CO2e")

    print("\nHuella por tipo de actividad:")
    por_tipo = calculadora.por_tipo()
    for tipo in por_tipo:
        print(f"   {tipo}: {por_tipo[tipo]:.1f} kg CO2e")


def ver_total(empresa):
    calculadora = CalculadoraHuella(empresa)
    print(f"\nTotal de {empresa.nombre}: {calculadora.total():.1f} kg CO2e")

    mayor = calculadora.departamento_mayor()
    if mayor is None:
        print("Todavía no hay departamentos.")
    else:
        print(f"Departamento con más emisiones: {mayor.nombre} "
              f"({mayor.calcular_emisiones():.1f} kg CO2e)")


def guardar(empresa):
    db = GestorDB()
    db.guardar_empresa(empresa)
    db.cerrar()
    print("Datos guardados en carbono.db")


def cargar(empresa):
    db = GestorDB()
    cargada = db.cargar_empresa(empresa.nombre)
    db.cerrar()

    if len(cargada.departamentos) == 0:
        print("No hay datos guardados de esta empresa.")
        return empresa

    print(f"Se cargaron {len(cargada.departamentos)} departamento(s).")
    return cargada


def main():
    nombre = input("Nombre de la empresa (Enter = EcoMex S.A.): ")
    if nombre.strip() == "":
        nombre = "EcoMex S.A."
    empresa = Empresa(nombre)

    opcion = ""
    while opcion != "0":
        mostrar_menu()
        opcion = input("Opción: ").strip()

        # Cada opción va dentro de try para que un dato mal escrito
        # muestre el error y no cierre el programa
        try:
            if opcion == "1":
                agregar_departamento(empresa)
            elif opcion == "2":
                registrar_actividad(empresa)
            elif opcion == "3":
                ver_huella(empresa)
            elif opcion == "4":
                ver_total(empresa)
            elif opcion == "5":
                guardar(empresa)
            elif opcion == "6":
                empresa = cargar(empresa)
            elif opcion == "0":
                print("Hasta luego.")
            else:
                print("Opción no válida.")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
