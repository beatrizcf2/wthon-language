from compilador.tables import *

# abstrato - nao posso implementar um objeto do tipo node, so dos seus filhos
class Node: 
    def __init__(self, value, children):
        self.value = value #str. tipo do token
        self.children = children #int. valor do token
    
    def evaluate():
        pass


class BinOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, st):
        left = (self.children[0]).evaluate(st)
        right = (self.children[1]).evaluate(st)
        
        if self.value == '.':
            return (str(left[0]) + str(right[0]), "string")
        elif self.value == '==':
            return (int(left[0] == right[0]), 'int')
        elif self.value == '>':
            return (int(left[0]>right[0]), 'int')
        elif self.value == '<':
            return (int(left[0]<right[0]), 'int')
        elif self.value == '&&':
            return (int(left[0] and right[0]), 'int')
        elif self.value == '||':
            return (int(left[0] or right[0]), 'int')
        elif left[1] == 'int' and right[1] == 'int':
            if self.value == '+':
                return (left[0]+right[0], 'int')
            elif self.value == '-':
                return (left[0]-right[0], 'int')
            elif self.value == '*':
                return (left[0]*right[0], 'int')
            elif self.value == '/':
                return (left[0]//right[0], 'int')
        else:
            raise Exception("Type mismatch")
        

class UnOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def evaluate(self, st):
        type = "int"
        if self.value == '+':
            return ((+(self.children[0]).evaluate(st)[0]), type)
        elif self.value == '-':
            return (-(self.children[0]).evaluate(st)[0], type)
        elif self.value == '!':
            return (not(self.children[0]).evaluate(st)[0], type)
        

class IntVal(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def evaluate(self, st):
        return (self.value, 'int')

class StrVal(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def evaluate(self, st):
        return (self.value, 'string')

class NoOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    def evaluate(self, st):
        pass

# editar para dar return de um valor !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!; 
class Block(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def evaluate(self, st):
        # vai fazer o evaluate de cada filho em ordem

        for child in self.children:
            if child.value == "Return":
                return child.evaluate(st)
            child.evaluate(st)

class VarDec(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def evaluate(self, st):
        # create symbol table
        type = self.value
        for child in self.children:
            st.create(child.value, type)
        
class Print(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def evaluate(self, st):
        print(self.children[0].evaluate(st)[0])


class Assignment(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def evaluate(self, st):
        #faz o evaluate so do filho da direita (filho 1)
        st.setter(self.children[0].value, self.children[1].evaluate(st)) 

class Identifier(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def evaluate(self, st):
        #Verifica symbol table
        return st.getter(self.value)
         
class Read(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def evaluate(self, st):
        return (int(input()), "int")

class While(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def evaluate(self, st):
        while self.children[0].evaluate(st)[0]:
            self.children[1].evaluate(st)

class If(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def evaluate(self, st):
        if self.children[0].evaluate(st)[0]:
            self.children[1].evaluate(st)
        else:
            if len(self.children) == 3:
                self.children[2].evaluate(st)

class FuncDec(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def evaluate(self, st):
        #filho 0: identifier
        FuncTable.create(self.children[0].value, self.value, self)
        #filho 1 a n: varDec
        #filho -1: block
        

class FuncCall(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def evaluate(self, st):
        # n filhos
        # verifica se a funcao existe
        func = FuncTable.getter(self.value)[1]
        # se existir, verifica se o numero de argumentos esta correto
        if (len(func.children)-2 == len(self.children)):
            # se estiver correto, cria uma nova symbol table
            st_func = SymbolTable()
            # coloca os argumentos (filhos do funcall) na symbol table
            for i in range(len(self.children)):
                func.children[i+1].evaluate(st_func) # create element symboltable
                # coloca o valor do argumento na symbol table
                st_func.setter(func.children[i+1].children[0].value, self.children[i].evaluate(st))

            
            # executa o bloco da funcao
            return func.children[-1].evaluate(st_func)
        else:
            raise Exception("Wrong number of arguments")
            

    

class Return(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def evaluate(self, st):
        for child in self.children:
            return child.evaluate(st)
