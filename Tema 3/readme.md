# Investigación: Lenguajes  y Gramáticas Formales

## Integrantes del Equipo
* **Frontado, Keiner**
* **Martínez, Giovanni** 
* **Morales, Edgar**
* **Ortega, Mansour**

El documento presenta una breve descripción de los núcleos temáticos desarrollados a lo largo del tercer informe de la unidad curricular **Lenguajes y Compiladores** 

---

## 1. Fundamentos Teóricos y Jerarquía de Chomsky
* **Estructuras Base:** Definición formal y matemática de componentes esenciales: **Alfabetos** como conjuntos finitos no vacíos, **Cadenas** (secuencias finitas de símbolos), **Clausura de Kleene** y el concepto de **Derivaciones** de cadenas.
* **Clasificación Automática:** Estudio de los cuatro niveles de la **Jerarquía de Chomsky (1956)**, diferenciando las capacidades y límites de:
  * Gramáticas Tipo 3 (Regulares - Autómatas Finitos)
  * Gramáticas Tipo 2 (Libres de Contexto - Autómatas de Pila)
  * Gramáticas Tipo 1 (Sensibles al Contexto - Autómatas Linealmente Acotados)
  * Gramáticas Tipo 0 (Sin Restricciones - Máquinas de Turing)

## 2. Modelado Cinemático y Aplicaciones Multidisciplinarias
* **Sistemas de Lindenmayer:** Aplicación de gramáticas paralelas para la modelación y generación de estructuras biológicas y fractales complejas.
* **Interpretación de Tortuga:** Traducción semántica de cadenas moleculares del **ADN** en operaciones vectoriales de movimiento y trayectorias geométricas.
* **Cinemática Inversa y Memoria:** Uso de operadores de retroceso y bifurcaciones balanceadas equivalentes al comportamiento operativo de una memoria de tipo **Pila**.

## 3. Patologías Gramaticales e Higiene del Compilador
* **Ambigüedad:** Identificación de gramáticas que producen múltiples árboles de análisis sintáctico para una misma cadena y su reescritura mediante precedencia explícita.
* **Recursividad Izquierda:** Diagnóstico de bucles infinitos en algoritmos de análisis descendente (Top-Down) y aplicación de fórmulas de eliminación.
* **Factorización:** Técnicas de reestructuración gramatical por factor común a la izquierda para garantizar el determinismo en el proceso de *parsing*.

## 4. Caso Práctico: Modelado Léxico de Notación PGN de Ajedrez
* **Formalización de Reglas:** Abstracción y simplificación del estándar *Portable Game Notation* (PGN) para capturar el subconjunto de movimientos y capturas válidas del ajedrez.
* **Diseño del Autómata:** Transición metodológica completa:
  1. Construcción de la **Expresión Regular (ER)** representativa del sublenguaje.
  2. Implementación y equivalencia mediante un **Autómata Finito Determinístico (AFD)** minimizado y libre de ambigüedades.

## 🎥 Defensas en Video
A continuación se especifican el enlace del video donde cada miembro del equipo JIT Research, detall los temas abordados para facilitar la comprensión del tema:

## https://youtu.be/BiDmOSkGSUU