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
