%{
// C Definitions
#include <stdio.h>
#include <string.h>
#include "wthon.tab.h"

void showError();
%}

/* Regular Expressions */
number      [0-9]+ 
string      [a-zA-Z]+
identifier  [a-zA-Z_][a-zA-Z0-9_]*
and         and|und|e 
or          or|oder|ou
not         not|nicht|nao
if          if|wenn|se
then        then|dann|entao
else        else|sonst|senao
while       while|solange|enquanto
def         def
return      return|zurueck|retorna
print       print|drucke|imprime
type        int|str
idiom       portuguese|english|deutsch


/* Tokens Specifications */
%%

"="             {return(EQUAL);}
";"             {return(SEMICOLON);}
","             {return(COMMA);}
"("             {return(LPAREN);}
")"             {return(RPAREN);}
"{"             {return(LBRACE);}
"}"             {return(RBRACE);}
"--"            {return(LANG);}

"+"             {return(PLUS);}
"-"             {return(MINUS);}
"*"             {return(TIMES);}
"/"             {return(DIVIDE);}
"."             {return(DOT);}
">"             {return(GT);}
"<"             {return(LT);}
"=="            {return(EQUALS);}

and             {return(AND);}
or              {return(OR);}
not             {return(NOT);}
if              {return(IF);}
else            {return(ELSE);}
while           {return(WHILE);}
def             {return(DEF);}
return          {return(RETURN);}
type            {return(TYPE);}
print           {return(PRINT);}
idiom           {return(IDIOM);}

[ \t]+          {/**/}


{number}        {yylval.number = atoi(yytext); return(NUM);}
{string}        {sscanf(yytext, "%s", yylval.name); return(STR);}
{identifier}    {sscanf(yytext, "%s", yylval.name); return(ID);}

.               {showError(); return(OTHER);}

%%

void showError()
{
    printf("Error: %s", yytext);
}

int yywrap()
{
    return 1;
}


