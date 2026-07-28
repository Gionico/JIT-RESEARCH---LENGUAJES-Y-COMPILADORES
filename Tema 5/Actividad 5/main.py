import sys
from lexer import lexer_hibrido
from parser_unegscript import ParserUnegScript, mostrar_ast

def ejecutar_asistente_unegscript(codigo_fuente):
    print("=" * 60)
    print("      ASISTENTE DE PROGRAMACIÓN HÍBRIDO - UNEGSCRIPT")
    print("=" * 60)
    print(f"\n📝 CÓDIGO DE ENTRADA:\n   {codigo_fuente}\n")

    # 1. Fase Léxica: Tokenización + Fallback por similitud/IA
    tokens, sugerencias_lexer = lexer_hibrido(codigo_fuente)

    print("------------------------------------------------------------")
    print(" 1. TOKENS CORREGIDOS")
    print("------------------------------------------------------------")
    for t_type, t_val in tokens:
        print(f"  [{t_type:<12}] -> '{t_val}'")

    # 2. Fase Sintáctica: Construcción del AST
    print("\n------------------------------------------------------------")
    print(" 2. ÁRBOL DE SINTAXIS ABSTRACTA (AST)")
    print("------------------------------------------------------------")
    try:
        parser = ParserUnegScript(tokens)
        ast = parser.parse()
        mostrar_ast(ast)
    except SyntaxError as err:
        print(f"❌ Error Sintáctico Detectado: {err}")
        sugerencias_lexer.append(f"Sugerencia Sintáctica: Verificar estructura o signos de puntuación faltantes.")

    # 3. Reporte Final de Sugerencias de la IA
    print("\n------------------------------------------------------------")
    print(" 3. SUGERENCIAS DE IA / REPORTE DE CORRECCIONES")
    print("------------------------------------------------------------")
    if sugerencias_lexer:
        for sug in sugerencias_lexer:
            print(f"  • {sug}")
    else:
        print("  • No se detectaron errores ni anomalías en el código.")
    print("=" * 60)


if __name__ == "__main__":
    # Entrada oficial requerida por la guía del Tema 5
    codigo_oficial = 'pront x=5; if x>3 prnt(x) else prnt("no")'
    
    # Permite pasar un código personalizado por argumento o usar el oficial por defecto
    if len(sys.argv) > 1:
        codigo_oficial = sys.argv[1]

    ejecutar_asistente_unegscript(codigo_oficial)