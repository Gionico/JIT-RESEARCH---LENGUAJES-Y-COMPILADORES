# Actividad 5: Asistente de Programación Híbrido (UnegScript)

**Asignatura:** Lenguajes y Compiladores  
**Tema:** Tema 5 (Análisis Sintáctico)  
**Institución:** Universidad Nacional Experimental de Guayana (UNEG)
**Desarrollador:** Edgar Morales  

---

## Descripción del Proyecto

Este proyecto implementa un **Asistente de Programación Híbrido** para un subconjunto del lenguaje Python denominado **UnegScript**. A diferencia de los compiladores deterministas tradicionales que colapsan ante errores de sintaxis o palabras clave mal escritas, este sistema integra una capa léxica con **tolerancia a fallas** combinada con un **Parser Recursivo Descendente** para la generación del Árbol de Sintaxis Abstracta (AST).

---

## Arquitectura y Componentes

El proyecto se divide en tres módulos principales escritos en **Python 3** utilizando la librería estándar (`re`, `difflib`) sin dependencias externas complejas:

| Archivo | Función Principal |
| :--- | :--- |
| **`lexer.py`** | Tokenizador léxico mediante RegEx con corrección ortográfica por similitud ($Ratio \ge 0.8$) y fallback por diccionario. |
| **`parser_unegscript.py`** | Parser recursivo descendente con capacidad de anticipación (*lookahead*) y definición de clases para los nodos del AST. |
| **`main.py`** | Script integrador que coordina la ejecución completa y formatea la salida en tres secciones estructuradas. |

---

## Flujo de Trabajo

1. **Fase Léxica (Lexer Híbrido):**
   * Tokeniza literales, operadores, delimitadores e identificadores mediante expresiones regulares.
   * Para identificadores que no coinciden exactamente con las palabras clave (`print`, `if`, `else`), calcula el ratio de coincidencia según la distancia de Levenshtein:
     $$\text{ratio} = 1 - \frac{\text{Distancia de Levenshtein}(s_1, s_2)}{\max(\text{len}(s_1), \text{len}(s_2))}$$
   * Si $\text{ratio} \ge 0.8$, aplica corrección automática a la palabra clave correspondiente[cite: 3, 6]. Si es menor, ejecuta un *fallback* a un diccionario de intenciones.

2. **Fase Sintáctica (Parser Descendente):**
   * Consume la secuencia de tokens normalizada utilizando las funciones `peek()` y `consume()`.
   * Instancia nodos jerárquicos en memoria (`ProgramNode`, `AssignNode`, `IfNode`, `PrintNode`, `BinOpNode`, `VarNode`, `LiteralNode`).

3. **Reporte Consolidado:**
   * Muestra los tokens finales corregidos, la representación jerárquica del AST y el desglose de sugerencias emitidas.

---

## Instrucciones de Ejecución

No se requieren instalaciones adicionales. Ejecuta el archivo principal desde la terminal de tu entorno Python 3:

```bash
python main.py
```

También es posible pasar un fragmento de código personalizado como argumento:

```bash
python main.py "pront y=10; if y>5 prnt(y)"
```

---

## 📌 Conclusiones

La implementación demuestra cómo la integración de técnicas de tolerancia a fallas en la fase inicial de compilación evita que el parser colapse prematuramente por errores ortográficos comunes, combinando la solidez de las gramáticas formales con la flexibilidad de las herramientas de desarrollo asistidas.
