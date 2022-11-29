class SymbolTable():
    # deixar table dinamica
    def __init__(self):
        self.table = {}

    def create(self, name, type):
        # verifica se a variavel ja existe
        if name in self.table:
            raise Exception(f"{name} Variable already exists")
        else: 
            if type == 'int':
                self.table[name] = (0, type)
            elif type == 'string':
                self.table[name] = ('', type)

    def getter(self, name):
        return self.table[name]

    def setter(self, name, value):
        # verifica se corresponde ao mesmo tipo
        print(value)
        if self.table[name][1] != value[1]:
            raise Exception(f"{name} Variable type mismatch")
        self.table[name] = value

class FuncTable():
    table = {}

    @staticmethod
    def create(name, type, *nodeRef):
        # verifica se a variavel ja existe
        if name in FuncTable.table:
            raise Exception("Function already exists")
        else: 
            FuncTable.table[name] = (type, *nodeRef)

    @staticmethod
    def getter(name):
        try:
            return FuncTable.table[name]
        except:
            raise Exception("Function not found")

    @staticmethod
    def setter(name, value):
        # verifica se corresponde ao mesmo tipo
        if FuncTable.table[name][0] != value[0]:
            raise
        FuncTable.table[name] = value

#classe de palavras reservadas
class ReservedTable():
    english_table = {
        'if': 'if',
        'else': 'else',
        'while': 'while',
        'int': 'int',
        'str': 'str',
        'print': 'print',
        'return': 'return',
        'function': 'function',
        'and': 'and',
        'or': 'or',
        'not': 'not',
    }

    portuguese_table = {
        'se': 'if',
        'senao': 'else',
        'enquanto': 'while',
        'int': 'int',
        'str': 'str',
        'imprime': 'print',
        'retorna': 'return',
        'funcao': 'function',
        'e': 'and',
        'ou': 'or',
        'nao': 'not'
    }

    german_table = {
        'wenn': 'if',
        'sonst': 'else',
        'solange': 'while',
        'int': 'int',
        'str': 'str',
        'drucke': 'print',
        'rückgabe': 'return',
        'funktion': 'function',
        'und': 'and',
        'oder': 'or',
        'nicht': 'not'
    }

    @staticmethod
    def get(name, idiom):
        if idiom == 'english':
            return ReservedTable.english_table[name]
        elif idiom == 'portuguese':
            return ReservedTable.portuguese_table[name]
        elif idiom == 'german':
            return ReservedTable.german_table[name]
