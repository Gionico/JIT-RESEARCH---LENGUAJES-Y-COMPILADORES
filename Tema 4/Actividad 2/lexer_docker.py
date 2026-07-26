import sys
import re

# ==============================================================================
# 1. DEFINICIÓN DE TOKENS MEDIANTE EXPRESIONES REGULARES
# ==============================================================================
# Cada tupla contiene (NOMBRE_TOKEN, PATRÓN_REGEX)
tokens = [
    # Palabras clave / Directivas principales de Dockerfile
    ('KW_FROM',        r'\bFROM\b'),
    ('KW_RUN',         r'\bRUN\b'),
    ('KW_CMD',         r'\bCMD\b'),
    ('KW_LABEL',       r'\bLABEL\b'),
    ('KW_EXPOSE',      r'\bEXPOSE\b'),
    ('KW_ENV',         r'\bENV\b'),
    ('KW_ADD',         r'\bADD\b'),
    ('KW_COPY',        r'\bCOPY\b'),
    ('KW_ENTRYPOINT',  r'\bENTRYPOINT\b'),
    ('KW_VOLUME',      r'\bVOLUME\b'),
    ('KW_USER',        r'\bUSER\b'),
    ('KW_WORKDIR',     r'\bWORKDIR\b'),
    ('KW_ARG',         r'\bARG\b'),
    ('KW_STOPSIGNAL',  r'\bSTOPSIGNAL\b'),
    ('KW_HEALTHCHECK', r'\bHEALTHCHECK\b'),
    ('KW_SHELL',       r'\bSHELL\b'),
    ('KW_AS',          r'\bAS\b'),
    
    # Flags opcionales (ej. --from=builder, --chown=user)
    ('FLAG',           r'--[a-zA-Z0-9_\-]+(=[a-zA-Z0-9_\-.\/]+)?'),
    
    # Cadenas entre comillas dobles o simples
    ('STRING',         r'"[^"\\]*(?:\\.[^"\\]*)*"|\'[^\'\\]*(?:\\.[^\'\\]*)*\''),
    
    # Delimitadores y Símbolos
    ('EQUALS',         r'='),
    ('COLON',          r':'),
    ('COMMA',          r','),
    ('LBRACKET',       r'\['),
    ('RBRACKET',       r'\]'),
    ('BACKSLASH',      r'\\'),
    
    # Números enteros (ej. puertos o códigos)
    ('NUMBER',         r'\b\d+\b'),
    
    # Identificadores, rutas, nombres de imagen y etiquetas (ej. python:3.10-slim, /app)
    ('IDENTIFIER',     r'[a-zA-Z0-9_\-./:]+'),
    
    # Elementos a ignorar o procesar por separado
    ('COMMENT',        r'#.*'),
    ('NEWLINE',        r'\n'),
    ('SKIP',           r'[ \t]+'),
    
    # Captura de caracteres no reconocidos (Errores Léxicos)
    ('MISMATCH',       r'.'),
]

# ==============================================================================
# 2. MOTOR DEL ANALIZADOR LÉXICO (LEXER)
# ==============================================================================
def lexer(input_text):
    # Compilación unificada de patrones regex con grupos nombrados
    token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in tokens)
    
    line_num = 1
    line_start = 0
    errors_found = 0

    print("=" * 75)
    print(f"{'TOKEN':<18} | {'LEXEMA':<30} | {'LÍNEA':<6} | {'COLUMNA':<6}")
    print("=" * 75)

    for mo in re.finditer(token_regex, input_text):
        kind = mo.lastgroup
        value = mo.group(kind)
        column = mo.start() - line_start + 1

        if kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
        elif kind == 'SKIP' or kind == 'COMMENT':
            continue  # Omitir espacios, tabulaciones y comentarios
        elif kind == 'MISMATCH':
            errors_found += 1
            print(f"ERROR LÉXICO: Carácter no reconocido '{value}' en Línea {line_num}, Columna {column}")
        else:
            print(f"{kind:<18} | {value:<30} | {line_num:<6} | {column:<6}")

    print("=" * 75)
    if errors_found > 0:
        print(f"Proceso finalizado con {errors_found} error(es) léxico(s).")
    else:
        print("Análisis léxico completado exitosamente sin errores.")
    print("=" * 75)

# ==============================================================================
# 3. PUNTO DE ENTRADA / LECTURA DE ARCHIVO
# ==============================================================================
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python3 lexer_docker.py <archivo_dockerfile>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            code = f.read()
        lexer(code)
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no existe.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
