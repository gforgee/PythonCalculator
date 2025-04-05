class Tokenizer:
    def __init__(self, expression: str):
        self.expression = expression.replace(" ", "")
        

    def tokenize(self) -> None:
        tokens = []
        number = ''
        if 'sqrt' in self.expression:
            self.expression = self.expression.replace('qrt', '')
        for char in self.expression:
            if char.isdigit() or char == '.':
                number += char
            elif char in ('+-*/()^'):
                if number:
                    tokens.append(number)
                    number = ''
                tokens.append(char)
            elif char == 's':
                tokens.append('s')
            
            else:
                raise ValueError(f"Nieznany znak: '{char}'")
              


        if number:
            tokens.append(number)

        self.tokens = tokens


    def get_info(self) -> list[str]:
        return self.tokens



class RPNConventer:
    def __init__(self,tokens: list[str]):
        self.tokens = tokens
        self.output = []

    def priority(self, op: str) -> int:
        if op in '-+':
            return 1
        elif op in '*/':
            return 2
        elif op == '^':
            return 3
        elif op == 's':
            return 3
        else:
            raise ValueError(f"Nieznany znak '{op}'")

    def convert(self):
        stack = []

        for char in self.tokens:
            if char.replace('.','', 1).isdigit():
                self.output.append(char)
            elif char in '+-*/^s':
                while stack and stack[-1] not in '()' and self.priority(stack[-1]) >= self.priority(char):
                    self.output.append(stack.pop())
                stack.append(char)

            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    self.output.append(stack.pop())
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    raise ValueError(f"Brakujacy nawias otwieracjacy")
            else:
                raise ValueError(f"Nieznany znak: {char}")
        while stack:
            if stack[-1] == '(':
                raise ValueError("Niewlasciwe nawiasy")
            self.output.append(stack.pop())

class ExpressionProcess:
    def __init__(self, expression: str):
        self.expression = expression
        tokenizer = Tokenizer(self.expression)
        tokenizer.tokenize()
        self.tokens = tokenizer.get_info()
        self.rpn = []
        converter = RPNConventer(self.tokens)
        converter.convert()
        self.rpn = converter.output 
    
    def get_result(self) -> list[str]:
        return self.rpn
        
        
if __name__ == "__main__":
    print('Szybki test')
    expr = "3 + 4 + 0.5    * 2 / (sqrt(5))(2)"
    print(expr)
    tokenizer = Tokenizer(expr)
    tokenizer.tokenize()
    tokens = tokenizer.get_info() 
    converter = RPNConventer(tokens)
    converter.convert()
    print("Tokeny wejściowe:", tokens)
    print("Wyjście RPN:", converter.output)
    #test Expression
    process = ExpressionProcess(expr)
    print('Wynik testu:',process.get_result())


