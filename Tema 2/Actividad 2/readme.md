# Actividad II: Conjetura de Collatz

## 1. Descripción general

Este repositorio contiene cuatro implementaciones del algoritmo de Collatz en los lenguajes:
- JavaScript (Node.js)
- Python
- Rust
- Zig

Cada implementación ejecuta una simulación de la secuencia de Collatz para valores de prueba y mide tiempo y consumo de memoria.

## 2. Versiones instaladas

- Zig: 0.13.0
- Python: 3.11.7
- Node.js: 22.16.0
- Rust/Cargo: 1.96.0

## 2.1 Ficha técnica del equipo utilizado

- Sistema operativo: Windows 10
- CPU: intel core i5-7500
- Memoria RAM instalada: 8GB DDR4 
- Almacenamiento: 512GB 

> Complete esta sección con los detalles del equipo utilizado para las pruebas.

## 3. Estructura de carpetas

- `JavaScript/main.js` → implementación con Node.js
- `python/main.py` → implementación con Python
- `rust/rust_benchmark/` → proyecto Rust con `Cargo.toml` y `src/main.rs`
- `zig/` → proyecto Zig con `build.zig` y `src/main.zig`

## 4. Cómo configurar el entorno

### 4.1 JavaScript

1. Instalar Node.js 22.16.0 o superior.
2. Desde `Tema 2/Actividad 2/JavaScript`, ejecutar:
   ```powershell
   node .\main.js
   ```

### 4.2 Python

1. Instalar Python 3.11.7.
2. Desde `Tema 2/Actividad 2/python`, ejecutar:
   ```powershell
   py .\main.py
   ```

### 4.3 Rust

1. Instalar Rust y Cargo 1.96.0.
2. Desde `Tema 2/Actividad 2/rust/rust_benchmark`, ejecutar:
   ```powershell
   cargo run --release
   ```

Cargo descargará automáticamente la dependencia `stats_alloc` indicada en `Cargo.toml`.

### 4.4 Zig

1. Instalar Zig 0.13.0.
2. Desde `Tema 2/Actividad 2/zig`, ejecutar:
   ```powershell
   zig build run -Doptimize=ReleaseFast
   ```

## 5. Reproducir el escenario de pruebas empíricas

Para cada lenguaje, ejecutar los comandos anteriores en su carpeta correspondiente. Los programas realizan una simulación de Collatz y muestran métricas de tiempo y memoria.

- JavaScript y Python usan un benchmark directo de un solo fichero.
- Rust usa `cargo run --release` para compilar en modo release y medir el rendimiento.
- Zig usa `zig build run -Doptimize=ReleaseFast` para compilar y ejecutar en modo `ReleaseFast`.

## 6. Resultados de pruebas

| n     | Lenguaje    | Tiempo (ms) | RAM (MB)    |
|-------|-------------|-------------|-------------|
| 5000  | JavaScript  | 532.0149    | 26.126051   |
| 5000  | Python      | 4222.5967   | 0.023397    |
| 5000  | Rust        | 509.4000    | 0.00791     |
| 5000  | Zig         | 511.6647    | 0.000061    |
| 10000 | JavaScript  | 1142.2960   | 45.665901   |
| 10000 | Python      | 10111.1300  | 0.026167    |
| 10000 | Rust        | 1012.8000   | 0.00791     |
| 10000 | Zig         | 1127.6699   | 0.000061    |
| 50000 | JavaScript  | 6804.8727   | 116.140936  |
| 50000 | Python      | 56718.6152  | 0.034247    |
| 50000 | Rust        | 6057.9000   | 0.00791     |
| 50000 | Zig         | 5785.3608   | 0.000061    |

