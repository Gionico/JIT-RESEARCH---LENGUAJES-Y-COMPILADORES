# 🚀 Actividad 5: Asistente de Programación Híbrido (UnegScript)

**Asignatura:** Lenguajes y Compiladores  
**Tema:** Tema 5 (Análisis Sintáctico)[cite: 6]  
**Institución:** Universidad Nacional Experimental de Guayana (UNEG)[cite: 6, 8]  
**Desarrollador:** Edgar Morales[cite: 8]  

---

## 📋 Descripción del Proyecto

Este proyecto implementa un **Asistente de Programación Híbrido** para un subconjunto del lenguaje Python denominado **UnegScript**[cite: 6]. A diferencia de los compiladores deterministas tradicionales que colapsan ante errores de sintaxis o palabras clave mal escritas[cite: 6, 8], este sistema integra una capa léxica con **tolerancia a fallas** combinada con un **Parser Recursivo Descendente** para la generación del Árbol de Sintaxis Abstracta (AST)[cite: 5, 6].

---

## 🛠️ Arquitectura y Componentes

El proyecto se divide en tres módulos principales escritos en **Python 3** utilizando la librería estándar (`re`, `difflib`) sin dependencias externas complejas[cite: 3]:

| Archivo | Función Principal |
| :--- | :--- |
| **`lexer.py`** | Tokenizador léxico mediante RegEx con corrección ortográfica por similitud ($Ratio \ge 0.8$) y fallback por diccionario[cite: 3, 6]. |
| **`parser_unegscript.py`** | Parser recursivo descendente con capacidad de anticipación (*lookahead*) y definición de clases para los nodos del AST[cite: 5, 6]. |
| **`main.py`** | Script integrador que coordina la ejecución completa y formatea la salida en tres secciones estructuradas[cite: 4]. |

---

## ⚙️ Flujo de Trabajo

1. **Fase Léxica (Lexer Híbrido):**
   * Tokeniza literales, operadores, delimitadores e identificadores mediante expresiones regulares[cite: 3].
   * Para identificadores que no coinciden exactamente con las palabras clave (`print`, `if`, `else`), calcula el ratio de coincidencia según la distancia de Levenshtein[cite: 3, 6]:
     $$\text{ratio} = 1 - \frac{\text{Distancia de Levenshtein}(s_1, s_2)}{\max(\text{len}(s_1), \text{len}(s_2))}$$
   * Si $\text{ratio} \ge 0.8$, aplica corrección automática a la palabra clave correspondiente[cite: 3, 6]. Si es menor, ejecuta un *fallback* a un diccionario de intenciones[cite: 3, 6].

2. **Fase Sintáctica (Parser Descendente):**
   * Consume la secuencia de tokens normalizada utilizando las funciones `peek()` y `consume()`[cite: 5].
   * Instancia nodos jerárquicos en memoria (`ProgramNode`, `AssignNode`, `IfNode`, `PrintNode`, `BinOpNode`, `VarNode`, `LiteralNode`)[cite: 5].

3. **Reporte Consolidado:**
   * Muestra los tokens finales corregidos, la representación jerárquica del AST y el desglose de sugerencias emitidas[cite: 4, 6].

---

## 🚀 Instrucciones de Ejecución

No se requieren instalaciones adicionales. Ejecuta el archivo principal desde la terminal de tu entorno Python 3[cite: 4]:

```bash
python main.py
```

También es posible pasar un fragmento de código personalizado como argumento[cite: 4]:

```bash
python main.py "pront y=10; if y>5 prnt(y)"
```

---

## 📌 Conclusiones

La implementación demuestra cómo la integración de técnicas de tolerancia a fallas en la fase inicial de compilación evita que el parser colapse prematuramente por errores ortográficos comunes[cite: 6, 8], combinando la solidez de las gramáticas formales con la flexibilidad de las herramientas de desarrollo asistidas[cite: 6, 8].
