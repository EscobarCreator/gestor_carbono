"""Clase GestorDB: guarda y carga las actividades de una empresa en SQLite.

Responsable: Juan Carlos
Sprint: 2
"""

import sqlite3

from modelos.empresa import Empresa
from modelos.departamento import Departamento
from modelos.actividad import ConsumoEnergetico, Transporte, Residuo


class GestorDB:
    """Guarda y carga las actividades de una empresa en una base SQLite."""

    def __init__(self, ruta="carbono.db"):
        # Abre la base de datos (si el archivo no existe, SQLite lo crea)
        self._conexion = sqlite3.connect(ruta)

        # Crea la tabla solo si todavía no existe
        self._conexion.execute(
            "CREATE TABLE IF NOT EXISTS actividades ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "empresa TEXT, "
            "departamento TEXT, "
            "clase TEXT, "
            "descripcion TEXT, "
            "cantidad REAL, "
            "tipo TEXT)"
        )
        self._conexion.commit()

    def guardar_empresa(self, empresa):
        # Primero borra lo que ya había guardado de esa empresa,
        # para no repetir actividades si se guarda dos veces
        self._conexion.execute(
            "DELETE FROM actividades WHERE empresa = ?",
            (empresa.nombre,)
        )

        # Recorre cada departamento y cada actividad, y guarda una fila por actividad
        for departamento in empresa.departamentos:
            for actividad in departamento.actividades:
                # Solo Transporte y Residuo tienen tipo; el consumo de luz no
                tipo = ""
                if isinstance(actividad, Transporte) or isinstance(actividad, Residuo):
                    tipo = actividad.tipo

                self._conexion.execute(
                    "INSERT INTO actividades "
                    "(empresa, departamento, clase, descripcion, cantidad, tipo) "
                    "VALUES (?, ?, ?, ?, ?, ?)",
                    (empresa.nombre, departamento.nombre, type(actividad).__name__,
                     actividad.descripcion, actividad.cantidad, tipo)
                )

        # Confirma los cambios en el archivo
        self._conexion.commit()

    def cargar_empresa(self, nombre):
        # Crea una empresa nueva y la va llenando con lo que hay en la tabla
        empresa = Empresa(nombre)

        filas = self._conexion.execute(
            "SELECT departamento, clase, descripcion, cantidad, tipo "
            "FROM actividades WHERE empresa = ?",
            (nombre,)
        ).fetchall()

        for fila in filas:
            nombre_departamento = fila[0]
            clase = fila[1]
            descripcion = fila[2]
            cantidad = fila[3]
            tipo = fila[4]

            # Si el departamento todavía no existe en la empresa, lo crea
            departamento = empresa.buscar_departamento(nombre_departamento)
            if departamento is None:
                departamento = Departamento(nombre_departamento)
                empresa.agregar_departamento(departamento)

            # Según la clase guardada, crea el objeto correcto
            if clase == "ConsumoEnergetico":
                actividad = ConsumoEnergetico(descripcion, cantidad)
            elif clase == "Transporte":
                actividad = Transporte(descripcion, cantidad, tipo)
            else:
                actividad = Residuo(descripcion, cantidad, tipo)

            departamento.agregar_actividad(actividad)

        return empresa

    def cerrar(self):
        # Cierra la conexión con la base de datos
        self._conexion.close()