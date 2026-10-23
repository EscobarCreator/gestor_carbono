# Gestor de Carbono Corporativo

Proyecto integrador de Programación Orientada a Objetos (UVM) · ODS 13 — Acción Climática.

Aplicación en Python que registra actividades de una empresa (consumo de energía, transporte y residuos), calcula su huella de carbono y recomienda cómo reducirla.

## Equipo

| Integrante | Rol |
| --- | --- |
| Emanuel Escobar Ríos | Scrum Master |
| Miguel Antonio Ramírez Gonzales | Developer Backend/POO |
| Ian Alejandro Chávez Cruz | Developer Backend/POO |
| Juan Carlos Moya Valenzuela | Developer Datos/Testing |
| Ángel Rojas Flores | Developer UI/Reportes |
| Prof. César Antonio Ríos Olivares | Product Owner |

## Cómo ejecutarlo

```bash
pip install -r requirements.txt
python main.py
```

## Cómo correr las pruebas

```bash
python -m pytest -v
```

## Estructura

```
gestor_carbono/
├── main.py            punto de entrada
├── modelos/           Empresa, Departamento, Actividad y sus hijas
├── servicios/         cálculo de huella y estrategias de reducción
├── datos/             base de datos SQLite
├── interfaz/          ventanas con Tkinter
├── reportes/          gráficas y reportes
├── tests/             pruebas con Pytest
└── docs/              UML y bocetos
```

## Cómo trabajamos en GitHub

1. Cada quien trabaja en su propia rama, nunca directo en `main`.
2. Para unir cambios se abre un Pull Request y el Scrum Master lo revisa.
3. Nunca se sube a `main` código que no corre.

```bash
git pull
git checkout -b tu-nombre-tarea
git add .
git commit -m "Describe lo que hiciste"
git push -u origin tu-nombre-tarea
```

## Sprints

| Sprint | Fechas | Meta |
| --- | --- | --- |
| 1 | 1–14 oct 2026 | Repositorio, UML y clases base |
| 2 | 15–28 oct 2026 | Registro de actividades, cálculo y base de datos |
| 3 | 29 oct–11 nov 2026 | Interfaz, gráficas, reportes y recomendaciones |
| 4 | 12–25 nov 2026 | Pruebas, manual y demo final |


## Uso del menú y la interfaz gráfica

El sistema cuenta con una interfaz gráfica desarrollada en Python con Tkinter, que permite navegar entre las diferentes secciones mediante un menú principal.

Al ejecutar el programa, se muestra un menú con cuatro opciones:

Inicio / Empresa: Permite ingresar el nombre de la empresa y agregar los departamentos que la conforman.

Registrar actividad: Permite seleccionar un departamento, elegir la clase de actividad (Luz, Transporte o Residuo), indicar el tipo, agregar una descripción e introducir la cantidad correspondiente. Al presionar el botón Guardar, se registra la información y se actualiza el total de emisiones de CO₂.

Resultados: Muestra el total de emisiones de CO₂ registradas, así como los resultados por departamento y una gráfica para visualizar la información.

Recomendaciones: Presenta consejos para reducir las emisiones contaminantes, como ahorrar electricidad, disminuir el consumo de combustibles y fomentar el reciclaje.

Cada sección incluye un botón Menú, que permite regresar a la pantalla principal sin necesidad de cerrar el programa.

## Pruebas de funcionamiento

Para comprobar el funcionamiento de la interfaz, se pueden realizar las siguientes pruebas:

Registrar una empresa y agregar diferentes departamentos.

Ingresar actividades de transporte, electricidad y residuos.

Verificar que el botón Guardar registre correctamente los datos.

Comprobar que el total de CO₂ se actualice al agregar nuevas actividades.

Revisar que los resultados se muestren correctamente por departamento.

Comprobar que los botones permitan navegar entre las pantallas.

Estas pruebas permiten verificar el funcionamiento básico de la interfaz y detectar posibles errores al introducir información.
