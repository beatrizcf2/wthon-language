# Wthon
Wthon is a global language. This project will implement thre different idioms: English, German and Portuguese.

# Example

```py
--english;
def HelloWorld(int n){
    int x;
    x = 0;
    while (x < n){
        print("Hello World: ");
        print(x);
        x = x + 1;
    };
};
HelloWorld(5);


--portugues;
def OlaMundo(int n){
    int x;
    x = 0;
    enquanto (x < n){
        imprime("Ola Mundo: ");
        imprime(x);
        x = x + 1;
    };
};
OlaMundo(5);


--deutsch;
def HalloWelt(int n){
    int x;
    x = 0;
    solange (x < n){
        drucke("Hallo Welt: ");
        drucke(x);
        x = x + 1;
    };
};
HalloWelt(5);
```
## EBNF

```TXT
BLOCK = "{", { STATEMENT }, "}";
STATEMENT = ( λ | ASSIGMENT | PRINT | DECLARATION| WHILE | IF | BLOCK | DEFINITION | FUNCTION);
DEFINITION = "def" , IDENTIFIER , "(" , DECLARATION , ")" , STATEMENT;
FUNCTION = IDENTIFIER , "(" , (IDENTIFIER | RELATIVE_EXPRESSION) , [{"," , (IDENTIFIER | RELATIVE_EXPRESSION)}] , ")" ;
ASSIGMENT = IDENTIFIER, "=", RELATIVE_EXPRESSION;
PRINT = ("print | "imprime" | "drucken"), "(", RELATIVE_EXPRESSION, ")";
WHILE = ( "while" | "enquanto" | "solange" ) , "(", RELATIVE_EXPRESSION , ")" , STATEMENT ;
IF = ( "if" | "se" | "wenn" ) , "(", RELATIVE_EXPRESSION , ")" , STATEMENT , [( "else" | "senao" | "sonst" ) , STATEMENT ] ;
DECLARATION = TYPE, IDENTIFIER, [{"," , IDENTIFIER}]; 
TYPE = ("int, str") ;
RELATIVE_EXPRESSION = EXPRESSION, { ( "==" | "<" | ">" ), EXPRESSION}; 
EXPRESSION = TERM, { ("+" | "-" | ("or" | "ou" | "oder") ), TERM}; 
TERM = FACTOR, { ("*" | "/" | ("and" | "e" | "und")), FACTOR};
FACTOR = (("+" | "-" | ("not"| "nao" | "nicht")), FACTOR) | NUMBER | STRING | "(", RELATIVE_EXPRESSION, ")" | IDENTIFIER | "-", "-", IDIOM;
NUMBER = DIGIT, { DIGIT };
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0) ;
STRING = LETTER, 
IDENTIFIER = LETTER, { LETTER | DIGIT | "_"} ; 
LETTER = ( a | ... | z | A | ... | Z) ;
IDIOM = ("portugues" | "english" | "deutsch" ) ;


```

```dotnetcli

bison --defines wthon.y
lex wthon.l
gcc -ll wthon.tab.c lex.yy.c
./a.out
```
