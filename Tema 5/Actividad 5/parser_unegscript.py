from lexer import lexer_hibrido  # Importa la función del Paso 1

# ==========================================
# 1. DEFINICIÓN DE LOS NODOS DEL AST
# ==========================================
class ASTNode:
    pass

class ProgramNode(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class AssignNode(ASTNode):
    def __init__(self, var_name, value_node):
        self.var_name = var_name
        self.value_node = value_node

class IfNode(ASTNode):
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

class PrintNode(ASTNode):
    def __init__(self, expr_node):
        self.expr_node = expr_node

class BinOpNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class VarNode(ASTNode):
    def __init__(self, name):
        self.name = name

class LiteralNode(ASTNode):
    def __init__(self, value, value_type):
        self.value = value
        self.value_type = value_type


# ==========================================
# 2. IMPLEMENTACIÓN DEL PARSER RECURSIVO
# ==========================================
class ParserUnegScript:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self, offset=0):
        """Mira el token actual sin avanzarlo (Lookahead)."""
        index = self.pos + offset
        if index < len(self.tokens):
            return self.tokens[index]
        return None

    def consume(self, expected_type=None):
        """Consume el token actual y avanza la posición."""
        token = self.peek()
        if token is None:
            raise SyntaxError("Error Sintáctico: Fin de archivo inesperado.")
        if expected_type and token[0] != expected_type:
            raise SyntaxError(f"Error Sintáctico: Se esperaba {expected_type} pero se encontró '{token[1]}'.")
        self.pos += 1
        return token

    def parse(self):
        """Punto de entrada principal para construir el AST."""
        statements = []
        while self.peek() is not None:
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
            # Omitir punto y coma si está presente
            if self.peek() and self.peek()[0] == "SEMI":
                self.consume("SEMI")
        return ProgramNode(statements)

    def parse_statement(self):
        """Analiza sentencias según la palabra clave inicial."""
        token = self.peek()
        if not token:
            return None

        tok_type = token[0]

        if tok_type == "KW_IF":
            return self.parse_if()
        elif tok_type == "KW_PRINT":
            return self.parse_print()
        elif tok_type == "IDENTIFIER":
            # Si el siguiente token es '=' es una asignación
            if self.peek(1) and self.peek(1)[0] == "ASSIGN":
                return self.parse_assign()
            return self.parse_expression()
        else:
            return self.parse_expression()

    def parse_assign(self):
        var_token = self.consume("IDENTIFIER")
        self.consume("ASSIGN")
        expr_node = self.parse_expression()
        return AssignNode(var_token[1], expr_node)

    def parse_print(self):
        self.consume("KW_PRINT")
        # Evalúa si la función print usa paréntesis o sintaxis directa
        has_paren = False
        if self.peek() and self.peek()[0] == "LPAREN":
            self.consume("LPAREN")
            has_paren = True
            
        expr = self.parse_expression()
        
        if has_paren:
            self.consume("RPAREN")
            
        return PrintNode(expr)

    def parse_if(self):
        self.consume("KW_IF")
        condition = self.parse_expression()
        then_branch = self.parse_statement()
        
        else_branch = None
        if self.peek() and self.peek()[0] == "KW_ELSE":
            self.consume("KW_ELSE")
            else_branch = self.parse_statement()
            
        return IfNode(condition, then_branch, else_branch)

    def parse_expression(self):
        left = self.parse_primary()
        
        if self.peek() and self.peek()[0] in ("OP_REL", "ASSIGN"):
            op_token = self.consume()
            right = self.parse_primary()
            
            # Manejar caso especial de asignación dentro de expresiones
            if op_token[0] == "ASSIGN" and isinstance(left, VarNode):
                return AssignNode(left.name, right)
            
            return BinOpNode(left, op_token[1], right)
            
        return left

    def parse_primary(self):
        token = self.peek()
        if not token:
            raise SyntaxError("Expresión incompleta.")
            
        tok_type, tok_val = token
        
        if tok_type == "NUMBER":
            self.consume("NUMBER")
            return LiteralNode(int(tok_val), "int")
        elif tok_type == "STRING":
            self.consume("STRING")
            return LiteralNode(tok_val, "str")
        elif tok_type == "IDENTIFIER":
            self.consume("IDENTIFIER")
            return VarNode(tok_val)
        else:
            raise SyntaxError(f"Elemento no reconocido en expresión: '{tok_val}'")


# ==========================================
# 3. FUNCIÓN VISUALIZADORA DEL AST
# ==========================================
def mostrar_ast(node, indent=0):
    prefix = "  " * indent
    if isinstance(node, ProgramNode):
        print(f"{prefix}ProgramNode:")
        for stmt in node.statements:
            mostrar_ast(stmt, indent + 1)
    elif isinstance(node, AssignNode):
        print(f"{prefix}AssignNode (var='{node.var_name}'):")
        mostrar_ast(node.value_node, indent + 1)
    elif isinstance(node, PrintNode):
        print(f"{prefix}PrintNode:")
        mostrar_ast(node.expr_node, indent + 1)
    elif isinstance(node, IfNode):
        print(f"{prefix}IfNode:")
        print(f"{prefix}  Condición:")
        mostrar_ast(node.condition, indent + 2)
        print(f"{prefix}  Rama THEN:")
        mostrar_ast(node.then_branch, indent + 2)
        if node.else_branch:
            print(f"{prefix}  Rama ELSE:")
            mostrar_ast(node.else_branch, indent + 2)
    elif isinstance(node, BinOpNode):
        print(f"{prefix}BinOpNode (op='{node.op}'):")
        mostrar_ast(node.left, indent + 1)
        mostrar_ast(node.right, indent + 1)
    elif isinstance(node, VarNode):
        print(f"{prefix}VarNode ('{node.name}')")
    elif isinstance(node, LiteralNode):
        print(f"{prefix}LiteralNode (val={node.value}, type={node.value_type})")


# --- PRUEBA DEL PASO 2 ---
if __name__ == "__main__":
    codigo_entrada = 'pront x=5; if x>3 prnt(x) else prnt("no")'
    
    # 1. Generar tokens
    tokens, sugerencias = lexer_hibrido(codigo_entrada)
    
    # 2. Construir AST
    parser = ParserUnegScript(tokens)
    ast = parser.parse()
    
    print("==================================================")
    print(" 3. ÁRBOL DE SINTAXIS ABSTRACTA (AST) GENERADO")
    print("==================================================")
    mostrar_ast(ast)