grammar DockerComposeNetwork;

// --- REGLAS SINTÁCTICAS (PARSER) ---
configFile : line* EOF ;

line
    : networksSection
    | servicesSection
    | keyValuePair
    | INDENT? keyValuePair
    | BLANK_LINE
    ;

networksSection : 'networks:' NEWLINE (INDENT networkDef)+ ;
networkDef      : ID ':' NEWLINE (INDENT INDENT netProperty)+ ;
netProperty     : ('driver' | 'attachable' | 'ipam' | 'driver_opts' | ID) ':' VALUE NEWLINE ;

servicesSection : 'services:' NEWLINE (INDENT serviceDef)+ ;
serviceDef      : ID ':' NEWLINE (INDENT INDENT serviceProperty)+ ;
serviceProperty : 'networks:' NEWLINE (INDENT INDENT INDENT ID)+
                | ID ':' VALUE NEWLINE ;

keyValuePair    : ID ':' VALUE NEWLINE ;

// --- REGLAS LÉXICAS (LEXER) ---
INDENT     : ('  ' | '\t')+ ;
ID         : [a-zA-Z_][a-zA-Z0-0_\-]* ;
VALUE      : [a-zA-Z0-9_\-./:"']+ ;
NEWLINE    : '\r'? '\n' ;
BLANK_LINE : [ \t]* NEWLINE ;
WS         : [ \t]+ -> skip ;
COMMENT    : '#' ~[\r\n]* -> skip ;