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
            self.next = Token('not', None)
            self.position += 3
        elif self.source[self.position:self.position+3] == "and":
            self.next = Token('and', None)
            self.position += 3
        elif self.source[self.position:self.position+5] == 'while':
            self.next = Token('while', None)
            self.position += 5
        elif self.source[self.position:self.position+2] == "if":
            self.next = Token('if', None)
            self.position += 2
        elif self.source[self.position:self.position+4] == "else":
            self.next = Token('else', None)
            self.position += 4
        elif self.source[self.position:self.position+4] == "read":
            self.next = Token('read', None)
            self.position += 4
        elif self.source[self.position:self.position+2] == "or":
            self.next = Token('or', None)
            self.position += 2
        elif self.source[self.position:self.position+5] == "print":
            self.next = Token('print', None)
            self.position += 5
        elif self.source[self.position:self.position+6] == "return":
            self.next = Token('return', None)
            self.position += 6
        elif self.source[self.position:self.position+8] == "function":
            self.next = Token('function', None)
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
            self.next = Token('identifier', characters)

        else:
            value = ''
            while character.isdigit():
                self.position += 1
                value += character
                if self.position < len(self.source):
                    character = self.source[self.position]
            self.next = Token('int', int(value))

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