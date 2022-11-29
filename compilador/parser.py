from compilador.nodes import *
from compilador.tokenizer import *

class Parser:
    tokenizer = None
    

    @staticmethod
    def parseProgram():
        filhos = []
        while Parser.tokenizer.next.type != 'eof':
            filhos.append(Parser.parseDeclaration())
        # get function main and call it
        filhos.append(FuncCall('Main', [])) 
        return Block('Block', filhos)

    @staticmethod
    def parseDeclaration():
        # retorna um funcDec que tem nfilhos: 
        # 0 - identifier
        # 1...n-2 - varDec
        # n-1 - block
        if Parser.tokenizer.next.type == 'lang_sel':
            Parser.tokenizer.selectNext()
            ReservedTable.changeIdiom(Parser.tokenizer.next.value)
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == 'semicolon':
                Parser.tokenizer.selectNext()
            else:
                raise Exception("Expected semicolon after lang_sel")
        varDecs = []
        if Parser.tokenizer.next.type == 'function':
            ReservedTable.get(Parser.tokenizer.next.type, Parser.tokenizer.next.value)
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == 'identifier':
                funcId = Identifier(Parser.tokenizer.next.value, [])
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == 'open':
                    Parser.tokenizer.selectNext()
                    if Parser.tokenizer.next.type == 'type':
                        type = Parser.tokenizer.next.value
                        Parser.tokenizer.selectNext()
                        if Parser.tokenizer.next.type == 'identifier':
                            id = Identifier(Parser.tokenizer.next.value, [])
                            varDecs.append(VarDec(type, [id]))
                            Parser.tokenizer.selectNext()
                            while Parser.tokenizer.next.type == 'comma':
                                Parser.tokenizer.selectNext()
                                if Parser.tokenizer.next.type == 'type':
                                    type = Parser.tokenizer.next.value
                                    Parser.tokenizer.selectNext()
                                    if Parser.tokenizer.next.type == 'identifier':
                                        id = Identifier(Parser.tokenizer.next.value, [])
                                        varDecs.append(VarDec(type, [id]))
                                        Parser.tokenizer.selectNext()
                                    else:
                                        raise Exception("Expected identifier after type")
                                else:
                                    raise Exception("Expected type after comma")
                        else:
                            raise Exception("Expected identifier after type")
                    if Parser.tokenizer.next.type == 'close':
                        Parser.tokenizer.selectNext()
                    else:
                        raise Exception("Expected close after variables declaration")
                    funcBlock = Parser.parseBlock()
                    filhos = [funcId] + varDecs + [funcBlock]
                    return FuncDec("function", filhos)
            else:
                raise Exception("Expected identifier")
        
               
        else:
            raise Exception("Expected function")


    @staticmethod
    def parseBlock():
        # Parser.tokenizer.selectNext()
        filhos = []
        if Parser.tokenizer.next.type == 'openblock':
            Parser.tokenizer.selectNext()
            while Parser.tokenizer.next.type != 'closeblock':
                filhos.append(Parser.parseStatement())
            Parser.tokenizer.selectNext()
            return Block('Block', filhos)
        else:
            raise Exception('Expected {')
    
    @staticmethod
    def parseStatement():
        if Parser.tokenizer.next.type == 'semicolon':
            Parser.tokenizer.selectNext()
            return NoOp('NoOp', [])
        elif Parser.tokenizer.next.type == 'identifier':
            id = Identifier(Parser.tokenizer.next.value, [])
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == 'atribuition':
                Parser.tokenizer.selectNext()
                token = Assignment('Assignment', [id, Parser.parseRelExpression()])
            elif Parser.tokenizer.next.type == 'open':
                Parser.tokenizer.selectNext()
                args = []
                while Parser.tokenizer.next.type != 'close':
                    args.append(Parser.parseRelExpression())
                    if Parser.tokenizer.next.type == 'comma':
                        Parser.tokenizer.selectNext()
                Parser.tokenizer.selectNext()
                token = FuncCall(id.value, args)
            if Parser.tokenizer.next.type == 'semicolon':
                Parser.tokenizer.selectNext()
                return token
            else:
                raise Exception('Expected ;')

        elif Parser.tokenizer.next.type == 'type':
            type = Parser.tokenizer.next.value
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == 'identifier':
                id = Identifier(Parser.tokenizer.next.value, [])
                ids = [id]
                Parser.tokenizer.selectNext()
                while Parser.tokenizer.next.type == 'comma':
                    Parser.tokenizer.selectNext()
                    if Parser.tokenizer.next.type == 'identifier':
                        ids.append(Identifier(Parser.tokenizer.next.value, []))
                        Parser.tokenizer.selectNext()
                    else:
                        raise Exception('Expected identifier after comma')
                
                if Parser.tokenizer.next.type == 'semicolon':
                    Parser.tokenizer.selectNext()
                    return VarDec(type, ids)
                else:
                    raise Exception('Expected ;')
            else:
                raise Exception('Expected identifier')

                    
        elif Parser.tokenizer.next.type == 'print':
            ReservedTable.get(Parser.tokenizer.next.type, Parser.tokenizer.next.value)
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == 'open':
                Parser.tokenizer.selectNext()
                filho = Parser.parseRelExpression()
                if Parser.tokenizer.next.type == 'close':
                    Parser.tokenizer.selectNext()
                    token = Print('Print', [filho])
                    if Parser.tokenizer.next.type == 'semicolon':
                        Parser.tokenizer.selectNext()
                        return token
                    else:
                        raise Exception('Expected ;')

        elif Parser.tokenizer.next.type == 'while':
            ReservedTable.get(Parser.tokenizer.next.type, Parser.tokenizer.next.value)
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == 'open':
                Parser.tokenizer.selectNext()
                filho = Parser.parseRelExpression()
                if Parser.tokenizer.next.type == 'close':
                    Parser.tokenizer.selectNext()
                    token = While('While', [filho, Parser.parseStatement()])
                    return token
        elif Parser.tokenizer.next.type == 'if':
            ReservedTable.get(Parser.tokenizer.next.type, Parser.tokenizer.next.value)
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == 'open':
                Parser.tokenizer.selectNext()
                filho = Parser.parseRelExpression()
                if Parser.tokenizer.next.type == 'close':
                    Parser.tokenizer.selectNext()
                    token = If('If', [filho, Parser.parseStatement()])
                    if Parser.tokenizer.next.type == 'else':
                        ReservedTable.get(Parser.tokenizer.next.type, Parser.tokenizer.next.value)
                        Parser.tokenizer.selectNext()
                        token.children.append(Parser.parseStatement())
                    return token
        elif Parser.tokenizer.next.type == 'return':
            ReservedTable.get(Parser.tokenizer.next.type, Parser.tokenizer.next.value)
            Parser.tokenizer.selectNext()
            token = Return('Return', [Parser.parseRelExpression()])
            if Parser.tokenizer.next.type == 'semicolon':
                Parser.tokenizer.selectNext()
                return token
            else:
                raise Exception('Expected ;')

        else:  
            return Parser.parseBlock()
        
        
    # criar Relative Expression
    @staticmethod
    def parseRelExpression():
        result = Parser.parseExpression()
        while Parser.tokenizer.next.type == "equal" or Parser.tokenizer.next.type == "greater" or Parser.tokenizer.next.type == "less" or Parser.tokenizer.next.type == "dot": # enquanto nao chegar no fim da minha str
            if Parser.tokenizer.next.type == 'equal':
                Parser.tokenizer.selectNext()
                result = BinOp('==', [result, Parser.parseExpression()])
            elif Parser.tokenizer.next.type == 'greater':
                Parser.tokenizer.selectNext()
                result = BinOp('>', [result, Parser.parseExpression()])
            elif Parser.tokenizer.next.type == 'less':
                Parser.tokenizer.selectNext()
                result = BinOp('<', [result, Parser.parseExpression()])
            elif Parser.tokenizer.next.type == 'dot':
                Parser.tokenizer.selectNext()
                result = BinOp('.', [result, Parser.parseExpression()])
        return result
    
    @staticmethod
    def parseExpression():
        result = Parser.parseTerm()
        while Parser.tokenizer.next.type == "plus" or Parser.tokenizer.next.type == "minus" or Parser.tokenizer.next.type == "or": # enquanto nao chegar no fim da minha str
            if Parser.tokenizer.next.type == 'plus':
                Parser.tokenizer.selectNext()
                result = BinOp('+', [result, Parser.parseTerm()])
            elif Parser.tokenizer.next.type == 'minus':
                Parser.tokenizer.selectNext()
                result = BinOp('-', [result, Parser.parseTerm()])
            elif Parser.tokenizer.next.type == 'or':
                ReservedTable.get(Parser.tokenizer.next.type, Parser.tokenizer.next.value)
                Parser.tokenizer.selectNext()
                result = BinOp('||', [result, Parser.parseTerm()])
        return result

    @staticmethod
    def parseTerm():
        # consome os tokens do tokenizer e analisa se a sintaxe está de acordo com a gramática
        # retorna o resultado da expressão analisada
        # enquanto nao chegar no fim da minha str
        result = Parser.parseFactor()
        token = Parser.tokenizer.next
        while token.type == "div" or token.type == "mult" or token.type == "and": # enquanto nao chegar no fim da minha str
            token = Parser.tokenizer.next
            if token.type == 'div':
                Parser.tokenizer.selectNext()
                result = BinOp('/', [result, Parser.parseFactor()])
            elif token.type == 'mult':
                Parser.tokenizer.selectNext()
                result = BinOp('*', [result, Parser.parseFactor()])
            elif token.type == 'and':
                Parser.tokenizer.selectNext()
                result = BinOp('&&', [result, Parser.parseFactor()])
        return result

    @staticmethod
    def parseFactor():
        token = Parser.tokenizer.next
        if token.type == 'plus':
            Parser.tokenizer.selectNext()
            return UnOp('+', [Parser.parseFactor()]) #filho é um nó retornado pelo parseFactor
        elif token.type == 'minus' :
            Parser.tokenizer.selectNext()
            return UnOp('-', [Parser.parseFactor()])
        elif token.type == 'not' :
            ReservedTable.get(Parser.tokenizer.next.type, Parser.tokenizer.next.value)
            Parser.tokenizer.selectNext()
            return UnOp('!', [Parser.parseFactor()])
        elif token.type == 'int':
            Parser.tokenizer.selectNext()
            return IntVal(token.value, []) #nao tem crianca
        elif token.type == 'identifier':
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == 'open':
                args = []
                Parser.tokenizer.selectNext()
                while Parser.tokenizer.next.type != 'close':
                    args.append(Parser.parseRelExpression())
                    if Parser.tokenizer.next.type == 'comma':
                        Parser.tokenizer.selectNext()
                Parser.tokenizer.selectNext()
                return FuncCall(token.value, args)
            return Identifier(token.value, []) # nao vai ter filhos -> leitura de identifier
        elif token.type == 'string':
            Parser.tokenizer.selectNext()
            return StrVal(token.value, [])
        elif token.type == 'open':
            Parser.tokenizer.selectNext()
            node = Parser.parseRelExpression() 
            if Parser.tokenizer.next.type == 'close':
                Parser.tokenizer.selectNext()
                return node 
        elif token.type == 'read':
            ReservedTable.get(Parser.tokenizer.next.type, Parser.tokenizer.next.value)
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == 'open':
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == 'close':
                    Parser.tokenizer.selectNext()
                    return Read('Read', [])
        elif token.type == 'eof':
            return
        else:
            raise

    @staticmethod
    def run(code):
        Parser.tokenizer = Tokenizer(code,0)
        Parser.tokenizer.selectNext()
        
        result = Parser.parseProgram() #retorna o root da arvore AST
        if Parser.tokenizer.next.type != "eof":
            raise
        return result