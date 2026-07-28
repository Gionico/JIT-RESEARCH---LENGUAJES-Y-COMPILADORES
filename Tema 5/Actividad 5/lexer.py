import re
from difflib import SequenceMatcher

# Conjunto de palabras clave oficiales del lenguaje UnegScript
KEYWORDS = {"print", "if", "else"}

# Definición de patrones léxicos mediante Expresiones Regulares
TOKEN_SPEC = [
    ("NUMBER",     r"\d+"),
    ("STRING",     r'"[^"]*"'),
    ("ASSIGN",     r"="),
    ("OP_REL",     r">|<|=="),
    ("SEMI",       r";"),
    ("LPAREN",     r"\("),
    ("RPAREN",     r"\)"),
    ("IDENTIFIER", r"[a-zA-Z_][a-zA-Z0-9_]*"),
    ("SKIP",       r"[ \t\n]+"),
    ("MISMATCH",   r"."),
]

def lexer_hibrido(codigo, umbral=0.8):
    """
    Analiza la cadena de texto, genera tokens y corrige palabras clave
    mal escritas según el umbral de confianza (>= 0.8).
    """
    tokens = []
    sugerencias_ia = []
    
    tok_regex = "|".join(f"(?P<{kind}>{pattern})" for kind, pattern in TOKEN_SPEC)
    
    for match in re.finditer(tok_regex, codigo):
        kind = match.lastgroup
        value = match.group()
        
        if kind == "SKIP":
            continue
            
        elif kind == "IDENTIFIER":
            if value in KEYWORDS:
                tokens.append(("KW_" + value.upper(), value))
            else:
                mejor_match = None
                max_ratio = 0.0
                
                for kw in KEYWORDS:
                    # Cálculo de similitud mediante ratio de Levenshtein/SequenceMatcher
                    ratio = SequenceMatcher(None, value, kw).ratio()
                    if ratio > max_ratio:
                        max_ratio = ratio
                        mejor_match = kw
                
                if max_ratio >= umbral:
                    sugerencias_ia.append(f"Sugerencia: '{value}' → '{mejor_match}' (Confianza: {max_ratio:.2f})")
                    tokens.append(("KW_" + mejor_match.upper(), mejor_match))
                else:
                    # Fallback de IA para tokens ambiguos por debajo de 0.8
                    fallback_diccionario = {"pront": "print", "prnt": "print"}
                    if value in fallback_diccionario:
                        correccion = fallback_diccionario[value]
                        sugerencias_ia.append(f"Sugerencia (Fallback IA): '{value}' → '{correccion}'")
                        tokens.append(("KW_" + correccion.upper(), correccion))
                    else:
                        tokens.append(("IDENTIFIER", value))
                        
        elif kind == "MISMATCH":
            sugerencias_ia.append(f"Alerta IA: Carácter no reconocido '{value}' ignorado.")
        else:
            tokens.append((kind, value))
            
    return tokens, sugerencias_ia


# --- PRUEBA DEL PASO 1 ---
if __name__ == "__main__":
    codigo_entrada = 'pront x=5; if x>3 prnt(x) else prnt("no")'
    
    tokens, sugerencias = lexer_hibrido(codigo_entrada)
    
    print("==================================================")
    print(" 1. LISTA DE TOKENS OBTENIDOS (CORREGIDOS)")
    print("==================================================")
    for t_type, t_val in tokens:
        print(f"  {t_type:<15} : '{t_val}'")
        
    print("\n==================================================")
    print(" 2. SUGERENCIAS Y REPORTE DE IA / FALLBACK")
    print("==================================================")
    for sug in sugerencias:
        print(f"  • {sug}")