# Actividad 2: Analizador Léxico para Dockerfiles

Este directorio contiene la solución para la **Actividad 2** del curso *Lenguajes y Compiladores*. Consiste en un analizador léxico (*lexer*) desarrollado en Python 3 para procesar y tokenizar la estructura de archivos de configuración `Dockerfile`.

---

## Archivos del Proyecto

* **`lexer_docker.py`**: Código fuente del analizador léxico desarrollado con expresiones regulares (`re`).
* **`Dockerfile.1`**: Prueba 1 — Configuración estándar de una aplicación Node.js.
* **`Dockerfile.2`**: Prueba 2 — Construcción en múltiples etapas (*Multi-stage build*) con Go y Alpine.
* **`Dockerfile.error`**: Prueba 3 — Caso de prueba para evaluar la detección de errores (`MISMATCH`) y coordenadas.

---

## Instrucciones de Ejecución

Para ejecutar el analizador en consola (WSL / Linux), utiliza los siguientes comandos:

```bash
# Caso de prueba 1 (Estándar)
python3 lexer_docker.py Dockerfile.1

# Caso de prueba 2 (Multi-stage)
python3 lexer_docker.py Dockerfile.2

# Caso de prueba 3 (Detección de errores)
python3 lexer_docker.py Dockerfile.error
