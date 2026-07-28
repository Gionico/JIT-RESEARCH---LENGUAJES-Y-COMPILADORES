%{
#include <stdio.h>
%}

%option noyywrap

%%

    /* 1. Palabras Reservadas */
"fn"            { printf("TOKEN: TK_FN          | Lexema: %s\n", yytext); }
"let"           { printf("TOKEN: TK_LET         | Lexema: %s\n", yytext); }
"mut"           { printf("TOKEN: TK_MUT         | Lexema: %s\n", yytext); }
"if"            { printf("TOKEN: TK_IF          | Lexema: %s\n", yytext); }
"else"          { printf("TOKEN: TK_ELSE        | Lexema: %s\n", yytext); }
"return"        { printf("TOKEN: TK_RETURN      | Lexema: %s\n", yytext); }

    /* 2. Tipos de datos */
"i32"|"f64"|"bool" { printf("TOKEN: TK_TYPE     | Lexema: %s\n", yytext); }
"true"|"false"     { printf("TOKEN: TK_BOOL_LIT | Lexema: %s\n", yytext); }

    /* 3. Operadores y Símbolos especiales */
"->"            { printf("TOKEN: TK_ARROW       | Lexema: %s\n", yytext); }
"=="            { printf("TOKEN: TK_EQ          | Lexema: %s\n", yytext); }
"="             { printf("TOKEN: TK_ASSIGN      | Lexema: %s\n", yytext); }
"+"|"-"|"*"|"/" { printf("TOKEN: TK_OP_MATH     | Lexema: %s\n", yytext); }
";"             { printf("TOKEN: TK_SEMICOLON   | Lexema: %s\n", yytext); }
":"             { printf("TOKEN: TK_COLON       | Lexema: %s\n", yytext); }
","             { printf("TOKEN: TK_COMMA       | Lexema: %s\n", yytext); }
"{"             { printf("TOKEN: TK_LBRACE      | Lexema: %s\n", yytext); }
"}"             { printf("TOKEN: TK_RBRACE      | Lexema: %s\n", yytext); }
"("             { printf("TOKEN: TK_LPAREN      | Lexema: %s\n", yytext); }
")"             { printf("TOKEN: TK_RPAREN      | Lexema: %s\n", yytext); }

    /* 4. Literales e Identificadores */
[0-9]+\.[0-9]+  { printf("TOKEN: TK_FLOAT_LIT   | Lexema: %s\n", yytext); }
[0-9]+          { printf("TOKEN: TK_INT_LIT     | Lexema: %s\n", yytext); }
[a-zA-Z_][a-zA-Z0-9_]* { printf("TOKEN: TK_ID   | Lexema: %s\n", yytext); }

    /* 5. Comentarios y Espacios en Blanco */
"//".*          { /* Ignorar comentarios de línea */ }
[ \t\n\r]+      { /* Ignorar espacios, tabulaciones y saltos */ }

    /* 6. Manejo de Errores Léxicos */
.               { printf("ERROR LÉXICO: Carácter no permitido '%s'\n", yytext); }

%%

int main(int argc, char **argv) {
    if (argc > 1) {
        FILE *archivo = fopen(argv[1], "r");
        if (!archivo) {
            perror("Error al abrir el archivo de entrada");
            return 1;
        }
        yyin = archivo;
    }
    yylex();
    return 0;
}