"""Interfaz grafica con Tkinter.

Responsable: Angel
Sprint: 2-3
"""

import tkinter as tk
from tkinter import ttk, messagebox

# Ventana principal
ventana = tk.Tk()
ventana.title("Sistema de emisiones CO2")
ventana.geometry("850x650")
ventana.configure(bg="white")

azul = "#087F91"
oscuro = "#164C56"

# Datos del sistema
departamentos = []
actividades = []
nombre_empresa = ""

# Factores de ejemplo (no oficiales)
factores = {
    "gasolina": 2.31,
    "diesel": 2.68,
    "relleno": 0.50,
    "reciclaje": 0.10,
    "electricidad": 0.40
}

def limpiar():
    for elemento in ventana.winfo_children():
        elemento.destroy()

def titulo(texto):
    tk.Label(
        ventana, text=texto,
        font=("Arial", 20, "bold"),
        fg=azul, bg="white"
    ).pack(pady=25)

def boton_menu():
    tk.Button(
        ventana, text="Menú",
        width=15, command=menu
    ).pack(pady=15)

def calcular_total():
    return sum(a["co2"] for a in actividades)

# PANTALLA 1: MENÚ
def menu():
    limpiar()
    titulo("MENÚ")

    tk.Label(
        ventana, text="Selecciona una opción:",
        font=("Arial", 13),
        fg=oscuro, bg="white"
    ).pack(pady=10)

    opciones = [
        ("1. Inicio / Empresa", empresa),
        ("2. Registrar actividad", actividad),
        ("3. Resultados", resultados),
        ("4. Recomendaciones", recomendaciones)
    ]

    for texto, funcion in opciones:
        tk.Button(
            ventana, text=texto,
            width=30, height=2,
            command=funcion
        ).pack(pady=10)

# PANTALLA 2: EMPRESA
def empresa():
    limpiar()
    titulo("INICIO / EMPRESA")

    tk.Label(
        ventana, text="Nombre de la empresa:",
        bg="white"
    ).pack()

    entrada_nombre = tk.Entry(ventana, width=40)
    entrada_nombre.insert(0, nombre_empresa)
    entrada_nombre.pack(pady=10)

    tk.Label(
        ventana, text="Lista de departamentos:",
        bg="white"
    ).pack(pady=10)

    lista = tk.Listbox(ventana, width=45, height=6)
    lista.pack()

    for departamento in departamentos:
        lista.insert(tk.END, departamento)

    entrada_departamento = tk.Entry(ventana, width=40)
    entrada_departamento.pack(pady=10)

    def agregar():
        global nombre_empresa

        nombre_empresa = entrada_nombre.get().strip()
        nuevo = entrada_departamento.get().strip()

        if nuevo and nuevo not in departamentos:
            departamentos.append(nuevo)
            lista.insert(tk.END, nuevo)
            entrada_departamento.delete(0, tk.END)
        else:
            messagebox.showwarning(
                "Aviso",
                "Escribe un departamento nuevo."
            )

    tk.Button(
        ventana, text="Agregar departamento",
        command=agregar
    ).pack(pady=10)

    boton_menu()

# PANTALLA 3: REGISTRAR ACTIVIDAD
def actividad():
    limpiar()
    titulo("REGISTRAR ACTIVIDAD")

    formulario = tk.Frame(ventana, bg="white")
    formulario.pack(pady=5)

    def campo(texto, fila):
        tk.Label(
            formulario, text=texto,
            bg="white", fg=oscuro
        ).grid(row=fila, column=0, padx=10, pady=10)

    campo("Departamento:", 0)
    combo_departamento = ttk.Combobox(
        formulario, values=departamentos,
        width=35, state="readonly"
    )
    combo_departamento.grid(row=0, column=1)

    campo("Clase:", 1)
    combo_clase = ttk.Combobox(
        formulario,
        values=["Luz", "Transporte", "Residuo"],
        width=35, state="readonly"
    )
    combo_clase.grid(row=1, column=1)

    campo("Tipo:", 2)
    combo_tipo = ttk.Combobox(
        formulario, width=35, state="readonly"
    )
    combo_tipo.grid(row=2, column=1)

    def cambiar_tipos(event=None):
        opciones = {
            "Luz": ["electricidad"],
            "Transporte": ["gasolina", "diesel"],
            "Residuo": ["relleno", "reciclaje"]
        }
        combo_tipo["values"] = opciones.get(
            combo_clase.get(), []
        )
        combo_tipo.set("")

    combo_clase.bind("<<ComboboxSelected>>", cambiar_tipos)

    campo("Descripción:", 3)
    entrada_descripcion = tk.Entry(
        formulario, width=38
    )
    entrada_descripcion.grid(row=3, column=1)

    campo("Cantidad:", 4)
    entrada_cantidad = tk.Entry(
        formulario, width=38
    )
    entrada_cantidad.grid(row=4, column=1)

    etiqueta_total = tk.Label(
        ventana,
        text=f"Total de CO2: {calcular_total():.2f} kg",
        font=("Arial", 13, "bold"),
        fg=azul, bg="white"
    )
    etiqueta_total.pack(pady=15)

    def guardar():
        departamento = combo_departamento.get()
        clase = combo_clase.get()
        tipo = combo_tipo.get()
        descripcion = entrada_descripcion.get().strip()

        try:
            cantidad = float(entrada_cantidad.get())

            if not departamento or not clase or not tipo:
                raise ValueError

            if cantidad <= 0:
                raise ValueError

            co2 = cantidad * factores[tipo]

            actividades.append({
                "departamento": departamento,
                "clase": clase,
                "tipo": tipo,
                "descripcion": descripcion,
                "cantidad": cantidad,
                "co2": co2
            })

            etiqueta_total.config(
                text=f"Total de CO2: {calcular_total():.2f} kg"
            )

            entrada_descripcion.delete(0, tk.END)
            entrada_cantidad.delete(0, tk.END)

            messagebox.showinfo(
                "Guardado",
                "Actividad registrada correctamente."
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Completa los campos e introduce una cantidad positiva."
            )

    tk.Button(
        ventana, text="Guardar",
        width=18, command=guardar
    ).pack(pady=10)

    boton_menu()

# PANTALLA 4: RESULTADOS
def resultados():
    limpiar()
    titulo("RESULTADOS")

    tk.Label(
        ventana,
        text=f"Total de CO2: {calcular_total():.2f} kg",
        font=("Arial", 16, "bold"),
        fg=azul, bg="white"
    ).pack(pady=15)

    tk.Label(
        ventana, text="Total de CO2 por departamentos:",
        font=("Arial", 13),
        fg=oscuro, bg="white"
    ).pack(pady=10)

    totales = {}

    for a in actividades:
        dep = a["departamento"]
        totales[dep] = totales.get(dep, 0) + a["co2"]

    for dep, total in totales.items():
        tk.Label(
            ventana,
            text=f"{dep}: {total:.2f} kg CO2",
            bg="white"
        ).pack(pady=5)

    tk.Label(
        ventana,
        text="Gráfica de emisiones por departamento",
        font=("Arial", 13, "bold"),
        bg="white", fg=oscuro
    ).pack(pady=15)

    # Gráfica sencilla con Canvas
    grafica = tk.Canvas(
        ventana, width=550, height=180,
        bg="white", highlightthickness=0
    )
    grafica.pack()

    if totales:
        maximo = max(totales.values())

        for i, (dep, total) in enumerate(totales.items()):
            y = 10 + i * 35

            if y + 25 > 180:
                break

            ancho = int((total / maximo) * 300)

            grafica.create_text(
                5, y + 10, text=dep, anchor="w"
            )
            grafica.create_rectangle(
                140, y, 140 + ancho, y + 20,
                fill=azul
            )
            grafica.create_text(
                150 + ancho, y + 10,
                text=f"{total:.1f}", anchor="w"
            )

    boton_menu()

# PANTALLA 5: RECOMENDACIONES
def recomendaciones():
    limpiar()
    titulo("RECOMENDACIONES")

    tk.Label(
        ventana, text="Lista de consejos:",
        font=("Arial", 14, "bold"),
        fg=oscuro, bg="white"
    ).pack(pady=15)

    consejos = [
        "1. Apagar luces y equipos que no se utilicen.",
        "2. Reducir el consumo de gasolina y diesel.",
        "3. Separar y reciclar los residuos.",
        "4. Promover el ahorro de energía en la empresa."
    ]

    for consejo in consejos:
        tk.Label(
            ventana, text=consejo,
            font=("Arial", 12),
            bg="white", fg=oscuro,
            wraplength=650
        ).pack(pady=15)

    boton_menu()

# Iniciar programa
menu()
ventana.mainloop()
