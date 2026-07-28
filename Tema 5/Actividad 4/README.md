# Analizador Léxico y Sintáctico para Interfaces de Red en Docker Compose (ANTLR v4)

**Universidad Nacional Experimental de Guayana (UNEG)**  
**Coordinación de Ingeniería en Informática**  
**Asignatura:** Lenguaje y Compiladores (2026-I)  
**Profesor:** Ing. Félix Márquez  

---

## 📋 Descripción del Proyecto

Este proyecto corresponde a la **Actividad 4** de la unidad de Análisis Sintáctico. El objetivo principal es diseñar e implementar un analizador léxico (*lexer*) y un analizador sintáctico (*parser*) para validar y procesar la estructura de interfaces de red descritas en archivos de configuración `docker-compose.yml`.

Además de la definición formal de la Gramática Libre de Contexto (GLC), el proyecto incluye un **experimento de carga** que mide y compara la latencia y eficiencia del parsing al procesar un dataset incremental de $n$ archivos ($5 < n < 20$) en tres entornos de ejecución distintos: **Python 3, Java (JVM) y C++**.

---

## 🛠️ Tecnologías y Herramientas

- **Metacompilador:** [ANTLR v4.13.1](https://www.antlr.org/) (Algoritmo $ALL(*)$)
- **Lenguaje Principal de Ejecución y Automatización:** Python 3.10+
- **Librerías de Python:**
  - `antlr4-python3-runtime` (Runtime de ejecución de ANTLR)
  - `antlr4-tools` (Generación CLI de parsers)
  - `matplotlib` (Generación de gráficas de rendimiento)
- **Entornos Evaluados en Benchmark:** Python 3, Java, C++

---

## 📁 Estructura del Repositorio

```text
proyecto_parser_docker/
│
├── DockerComposeNetwork.g4     # Especificación formal de la Gramática (Lexer + Parser)
├── generate_dataset.py        # Script que genera el dataset incremental de pruebas
├── run_benchmark.py           # Script principal de medición y generación de gráficas
│
├── test_files/                # Dataset con los 10 archivos docker_compose_*.yml
│   ├── docker_compose_1.yml
│   ├── ...
│   └── docker_compose_10.yml
│
├── DockerComposeNetworkLexer.py   # Archivos generados automáticamente por ANTLR4
├── DockerComposeNetworkParser.py  #
│
├── grafica_rendimiento_docker.png # Gráfica resultante del experimento de carga
└── README.md                      # Documentación del proyecto