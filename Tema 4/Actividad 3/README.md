# Analizador Léxico para un Subconjunto de Rust ($L$) usando Flex

Este carpeta contiene la implementación de un **analizador léxico (*lexer*)** desarrollado con el metacompilador **Flex** para un subconjunto formal del lenguaje de programación **Rust**, denominado **Lenguaje $L$**. 

Forma parte de la **Actividad 3 del Tema 4 (Análisis Léxico)** 

## 📁 Archivos

* **`lexer_rust.l`**: Archivo de especificación de Flex conteniendo las expresiones regulares, reglas de tokenización y la función principal `main` en C.
* **`prueba.rs`**: Archivo fuente en subconjunto de Rust utilizado como prueba para verificar el correcto funcionamiento del lexer.
* **`README.md`**: Guía completa de especificación, instalación, compilación y ejecución.

---

## 🔤 Especificación del Lenguaje $L$ (Subconjunto de Rust)

El analizador reconoce las siguientes categorías léxicas dentro del subconjunto $L$:

| Categoria | Token | Patrón / Lexemas Reconocidos |
| :--- | :--- | :--- |
| **Palabras Reservadas** | `TK_FN`, `TK_LET`, `TK_MUT`, `TK_IF`, `TK_ELSE`, `TK_RETURN` | `fn`, `let`, `mut`, `if`, `else`, `return` |
| **Tipos de Datos** | `TK_TYPE` | `i32`, `f64`, `bool` |
| **Literales Booleanos** | `TK_BOOL_LIT` | `true`, `false` |
| **Literales Numéricos** | `TK_INT_LIT`, `TK_FLOAT_LIT` | Enteros (`10`, `42`) y Flotantes (`3.14`) |
| **Identificadores** | `TK_ID` | Nombres de variables y funciones (`sumar`, `a`, `resultado`) |
| **Operadores** | `TK_ASSIGN`, `TK_EQ`, `TK_OP_MATH`, `TK_ARROW` | `=`, `==`, `+`, `-`, `*`, `/`, `->` |
| **Delimitadores** | `TK_SEMICOLON`, `TK_COLON`, `TK_COMMA`, `TK_LBRACE`, `TK_RBRACE`, `TK_LPAREN`, `TK_RPAREN` | `;`, `:`, `,`, `{`, `}`, `(`, `)` |
| **Ignorados** | N/A | Comentarios de línea (`//...`), espacios, tabulaciones y saltos de línea |
| **Errores Léxicos** | `ERROR LÉXICO` | Cualquier carácter no contemplado en el alfabeto de $L$ |

---

## 🛠️ Requisitos de Instalación

Para compilar y ejecutar este proyecto se requiere contar con las herramientas **Flex** (o **WinFlexBison**) y un compilador de C (**GCC**).

### En Windows:
* Descargar WinFlexBison (win_flex.exe)
* Contar con GCC instalado mediante MinGW, w64devkit o utilizar el entorno WSL (Windows Subsystem for Linux).

## 💻 Compilación y Ejecución en Windows
1) Generar el archivo C con WinFlex
```bash
winflex.exe lexer_rust.l
```
**(este comando genera el archivo `lex.yy.c`)**

2) Compilar el archivo C generado
```bash
gcc lex.yy.c -o lexer_rust
```
**(este comando genera el archivo ejecutable `lexer_rust`)**

3) ejecutar el lexer con un archivo de prueba
```bash
lexer_rust prueba.rs
```

## Ejemplo de Prueba y Salida Esperada
**Archivo de entrada (prueba.rs):**
```rust
// Archivo de prueba
fn sumar(a: i32, b: i32) -> i32 {
    let mut resultado: i32 = a + b;
    return resultado;
}
```
**Salida esperada del lexer:**
```
TOKEN: TK_FN          | Lexema: fn
TOKEN: TK_ID          | Lexema: sumar
TOKEN: TK_LPAREN      | Lexema: (
TOKEN: TK_ID          | Lexema: a
TOKEN: TK_COLON       | Lexema: :
TOKEN: TK_TYPE        | Lexema: i32
TOKEN: TK_COMMA       | Lexema: ,
TOKEN: TK_ID          | Lexema: b
TOKEN: TK_COLON       | Lexema: :
TOKEN: TK_TYPE        | Lexema: i32
TOKEN: TK_RPAREN      | Lexema: )
TOKEN: TK_ARROW       | Lexema: ->
TOKEN: TK_TYPE        | Lexema: i32
TOKEN: TK_LBRACE      | Lexema: {
TOKEN: TK_LET         | Lexema: let
TOKEN: TK_MUT         | Lexema: mut
TOKEN: TK_ID          | Lexema: resultado
TOKEN: TK_COLON       | Lexema: :
TOKEN: TK_TYPE        | Lexema: i32
TOKEN: TK_ASSIGN      | Lexema: =
TOKEN: TK_ID          | Lexema: a
TOKEN: TK_OP_MATH     | Lexema: +
TOKEN: TK_ID          | Lexema: b
TOKEN: TK_SEMICOLON   | Lexema: ;
TOKEN: TK_RETURN      | Lexema: return
TOKEN: TK_ID          | Lexema: resultado
TOKEN: TK_SEMICOLON   | Lexema: ;
TOKEN: TK_RBRACE      | Lexema: }
```
