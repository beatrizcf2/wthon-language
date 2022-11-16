%{
#include <stdio.h>

int yylex();
int yyerror(char *s);

%}

%token NUM STR ID 
%token EQUAL SEMICOLON COMMA LPAREN RPAREN LBRACE RBRACE LANG
%token PLUS MINUS TIMES DIVIDE DOT GT LT EQUALS AND OR NOT
%token IF ELSE WHILE RETURN DEF TYPE PRINT IDIOM
%token OTHER

%type <name> STR
%type <number> NUM

%union {
    char name[20];
    int number;
}

%%
prog:
    blck
;

blck:
    LBRACE stmt RBRACE

stmt:
    empty SEMICOLON
    | ID EQUAL relExpr SEMICOLON
    | declaration SEMICOLON
    | DEF ID LPAREN declaration RPAREN LBRACE stmt RBRACE
    | PRINT LPAREN relExpr RPAREN SEMICOLON
    | WHILE LPAREN relExpr RPAREN stmt
    | blck
    | IF LPAREN relExpr RPAREN stmt ELSE stmt
    | RETURN relExpr SEMICOLON
    | ID LPAREN relExpr RPAREN SEMICOLON

empty:
    /* empty */

declaration:
    TYPE ID
    | TYPE ID COMMA declaration

relExpr:
    expr
    | expr LT expr
    | expr GT expr
    | expr EQUALS expr

expr:
    term
    | expr PLUS term
    | expr MINUS term
    | expr OR term

term:
    factor
    | term TIMES factor
    | term DIVIDE factor
    | term AND factor

factor:
    LPAREN relExpr RPAREN
    | NUM
    | ID
    | STR
    | NOT factor
    | MINUS factor
    | PLUS factor
    | LANG IDIOM

;

%%

int yyerror(char *s) {
    fprintf(stderr, "error: %s\n", s);
    return 0;
}

int main() {
    yyparse();
    return 0;
}












