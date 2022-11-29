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
            if name == 'Main':
                name = ReservedTable.getMain()
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
        'print': 'print',
        'return': 'return',
        'function': 'function',
        'and': 'and',
        'or': 'or',
        'not': 'not',
        'read': 'read',
        'int': 'int',
        'str': 'str',
        'Main': 'Main',
        'eof': 'eof'
        
    }

    portuguese_table = {
        'if': 'se',
        'else': 'senao',
        'while': 'enquanto',
        'print': 'imprime',
        'return': 'retorne',
        'function': 'funcao',
        'and': 'e',
        'or': 'ou',
        'not': 'nao',
        'read': 'leia',
        'Main': 'Principal'
    }

    german_table = {
        'if': 'wenn',
        'else': 'sonst',
        'while': 'solange',
        'print': 'drucken',
        'return': 'gibzurueck',
        'function': 'funktion',
        'and': 'und',
        'or': 'oder',
        'not': 'nicht',
        'read': 'lese',
        'Main': 'HauptProgramm'
    }
    

    table = english_table #default

    @staticmethod
    def changeIdiom(idiom):
        if idiom == 'english':
            ReservedTable.table = ReservedTable.english_table
        elif idiom == 'portugues':
            ReservedTable.table = ReservedTable.portuguese_table
        elif idiom == 'deutsch':
            ReservedTable.table = ReservedTable.german_table
        else:
            raise Exception("Idiom not found")
        print(ReservedTable.table)

    @staticmethod
    def get(type, value):
        if ReservedTable.table[type] == value:
            return ReservedTable.table[type]
        else:
            print(type, value)
            raise Exception("Reserved word not found in this idiom")
    
    @staticmethod
    def getMain():
        return ReservedTable.table['Main']

    