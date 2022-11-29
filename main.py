from abc import abstractmethod
from compilador.parser import *
from compilador.tokenizer import *

def main(code):
    # porco, mas funciona para verificar vazio
    if len(code) <= 3:
        raise
    st = SymbolTable()
    #print(Parser.run(code).children)
    (Parser.run(code)).evaluate(st)

if __name__=="__main__":
    import sys
    # with open(sys.argv[1]) as f:
    #     source = f.read()

    with open('testes/soma.carbon') as f:
        source = f.read()
   
    code = PrePro.filter(source) + " eof"
    main(code)


    
