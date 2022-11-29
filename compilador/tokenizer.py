
class Token: 
    def __init__(self, type, value):
        self.type = type #str. tipo do token
        self.value = value #int. valor do token

class Tokenizer:

    def __init__(self, source, position):
        self.source = source #str. codigo fonte que sera tokenizado
        self.position = position #int. posicao atual no codigo fonte que o tokenizador esta separando
        self.next = None #Token. o ultimo token separado

    def selectNext(self):
        # Método que lê o próximo token e atualiza o atributo next
        character = self.source[self.position] #pega o primeiro caractere
        # symbols -------------------------------------
        while character == ' ':
            self.position += 1
            character = self.source[self.position]
        if character == '+':
            self.next = Token('plus', None)
            self.position += 1
        elif character == '-':
            self.position += 1
            if self.source[self.position] == '-':
                self.next = Token('lang_sel', None)
                self.position += 1

            else:
                self.next = Token('minus', None)
        elif character == '*':
            self.next = Token('mult', None)
            self.position += 1
        elif character == '/':
            self.next = Token('div', None)
            self.position += 1
        elif character == '(':
            self.next = Token('open', None)
            self.position += 1
        elif character == ')':
            self.next = Token('close', None)
            self.position += 1
        elif self.source[self.position:self.position+2] == "==":
            self.next = Token('equal', None)
            self.position += 2
        elif character == '=':
            self.next = Token('atribuition', None)
            self.position += 1
        elif character == ';':
            self.next = Token('semicolon', None)
            self.position += 1
        elif character == '{':
            self.next = Token('openblock', None)
            self.position += 1
        elif character == '}':
            self.next = Token('closeblock', None)
            self.position += 1
        elif character == ",":
            self.next = Token('comma', None)
            self.position += 1
        elif character == ":":
            self.next = Token('colon', None)
            self.position += 1
        elif character == ".":
            self.next = Token('dot', None)
            self.position += 1
        elif character == ">":
            self.next = Token('greater', None)
            self.position += 1
        elif character == "<":
            self.next = Token('less', None)
            self.position += 1

        # reserved words -------------------------------
        elif self.source[self.position:self.position+3] == "int":            
            self.next = Token('type', "int")
            self.position += 3
        elif self.source[self.position:self.position+3] == "str":
            self.next = Token('type', "string")
            self.position += 3

        elif  self.source[self.position:self.position+3] == "not":
            self.next = Token('not', "not")
            self.position += 3
        elif  self.source[self.position:self.position+5] == "nicht":
            self.next = Token('not', "nicht")
            self.position += 5
        elif self.source[self.position:self.position+3] == "nao":
            self.next = Token('not', "nao")
            self.position += 3


        elif self.source[self.position:self.position+5] == 'while':
            self.next = Token('while', "while")
            self.position += 5
        elif self.source[self.position:self.position+8] == 'enquanto':
            self.next = Token('while', "enquanto")
            self.position += 8
        elif self.source[self.position:self.position+7] == 'solange':
            self.next = Token('while', "solange")
            self.position += 7

        elif self.source[self.position:self.position+4] == "else":
            self.next = Token('else', "else")
            self.position += 4
        elif self.source[self.position:self.position+5] == "senao":
            self.next = Token('else', "senao")
            self.position += 5
        elif self.source[self.position:self.position+5] == "sonst":
            self.next = Token('else', "sonst")
            self.position += 5
            
        elif self.source[self.position:self.position+2] == "if":
            self.next = Token('if', "if")
            self.position += 2
        elif self.source[self.position:self.position+2] == "se":
            self.next = Token('if', "se")
            self.position += 2
        elif self.source[self.position:self.position+4] == "wenn":
            self.next = Token('if', "wenn")
            self.position += 4


        elif self.source[self.position:self.position+4] == "read":
            self.next = Token('read', "read")
            self.position += 4
        elif self.source[self.position:self.position+4] == "leia":
            self.next = Token('read', "leia")
            self.position += 4
        elif self.source[self.position:self.position+4] == "lese":
            self.next = Token('read', "lese")
            self.position += 4

        elif self.source[self.position:self.position+2] == "or":
            self.next = Token('or', "or")
            self.position += 2
        elif self.source[self.position:self.position+2] == "ou":
            self.next = Token('or', "ou")
            self.position += 2
        elif self.source[self.position:self.position+4] == "oder":
            self.next = Token('or', "oder")
            self.position += 4

        elif self.source[self.position:self.position+5] == "print":
            self.next = Token('print', "print")
            self.position += 5
        elif self.source[self.position:self.position+7] == "imprime":
            self.next = Token('print', "imprime")
            self.position += 7
        elif self.source[self.position:self.position+7] == "drucken":
            self.next = Token('print', "drucken")
            self.position += 7
        
        elif self.source[self.position:self.position+6] == "return":
            self.next = Token('return', "return")
            self.position += 6
        elif self.source[self.position:self.position+7] == "retorne":
            self.next = Token('return', "retorne")
            self.position += 7
        elif self.source[self.position:self.position+10] == "gibzurueck":
            self.next = Token('return', "gibzurueck")
            self.position += 10

        elif self.source[self.position:self.position+8] == "function":
            self.next = Token('function', "function")
            self.position += 8
        elif self.source[self.position:self.position+6] == "funcao":
            self.next = Token('function', "funcao")
            self.position += 6
        elif self.source[self.position:self.position+8] == "funktion":
            self.next = Token('function', "funktion")
            self.position += 8


        elif self.source[self.position:self.position+3] == "eof":
            self.next = Token('eof', None)
        
        elif character == '"':
            self.position += 1
            characters = ""
            character = self.source[self.position]
            while character!='"' and self.position < len(self.source):
                self.position += 1
                characters += character
                character = self.source[self.position]
            self.position+=1
           
            self.next = Token('string', characters)
        
        elif character.isalpha():
            characters = self.source[self.position]
            self.position += 1
            character = self.source[self.position]
            while character.isalpha() or character.isdigit() or character == '_': 
                self.position += 1
                characters += character
                if self.position < len(self.source):
                    character = self.source[self.position]
            if characters == "english" or characters == "portugues" or characters == "deutsch":
                self.next = Token('idiom', characters)
            # elif not Tokenizer.isReserved(characters): 
            else: 
                self.next = Token('identifier', characters)
                
        

        elif self.source[self.position:self.position+3] == "and":
            self.next = Token('and', "and")
            self.position += 3
        elif self.source[self.position:self.position+3] == "und":
            self.next = Token('and', "und")
            self.position += 3
        elif self.source[self.position:self.position+1] == "e":
            self.next = Token('and', "e")
            self.position += 1
        
        else:
            value = ''
            while character.isdigit():
                self.position += 1
                value += character
                if self.position < len(self.source):
                    character = self.source[self.position]
            self.next = Token('int', int(value))

        self.isIdentifier()
        #print(self.next.type, self.next.value)
        

    @staticmethod
    def isReserved(word):
        reserved = [
            'if', 'se', 'wenn',
            'else', 'senao', 'sonst',
            'while', 'enquanto', 'solange',
            'print', 'imprime', 'drucken',
            'return', 'retorne', 'gibzurueck',
            'function', 'funcao', 'funktion',
            'and', 'und', 'e',
            'or', 'ou', 'oder',
            'not', 'nao', 'nicht',
            'read', 'leia', 'lese',
            'int',
            'str',
            'eof'
        ]
        return word in reserved

    def isIdentifier(self):
        special = ['+', '-', '*', '/', '(', ')', '{', '}', '=', '<', '>', ',', ';','.', ' ']
        if Tokenizer.isReserved(self.next.value) and (self.source[self.position:self.position+1] not in special):
            print(self.next.type, self.next.value)
            print("debug: ", self.source[self.position:self.position+1])
            print("debug: ", Tokenizer.isReserved(self.next.value) and self.source[self.position:self.position+1] != ' ' )
            self.position -= len(self.next.value)
            characters = self.source[self.position]
            self.position += 1
            character = self.source[self.position]
            while character.isalpha() or character.isdigit() or character == '_': 
                self.position += 1
                characters += character
                if self.position < len(self.source):
                    character = self.source[self.position]
            self.next = Token('identifier', characters)
            print(self.next.type, self.next.value)

        

class PrePro():
    @staticmethod
    def filter(code):
        import re
        #primeiro remove os comentarios
        #segundo remove \n e \t
        if code.isspace():
            raise
        code = re.sub(re.compile("//.*?\n" ) ,"" ,code) # remove all occurance singleline comments (//COMMENT\n ) from string
        code = re.sub(r'\n', '', code)
        code = re.sub(r'\t', '', code)
        return code