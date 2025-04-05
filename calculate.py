from math import pow
class Calculate:
    def __init__(self, rpn_tokens: list[str]):
        self.rpn_tokens = rpn_tokens
    def evaluate(self) -> list[str]:
        stack = []
        num1 = 0
        num2 = 0
        for token in self.rpn_tokens:
            try:
                stack.append(float(token))
            except ValueError:
                if (token in '+-*/^'):
                    if len(stack) > 1:
                        num1 = stack.pop()
                        num2 = stack.pop()
                        if token == '+':
                            stack.append(num2 + num1)
                        elif token == '-':
                            stack.append(num2 - num1)
                        elif token == '*':
                            stack.append(num2 * num1)
                        elif token == '/':
                            stack.append(num2 / num1)
                        elif token == '^':
                            stack.append(pow(num2, num1))
                    else:
                        raise ValueError("Not enough operands for operation")
                elif token == 's':
                    if len(stack) > 0:
                        num1 = stack.pop()
                        stack.append(num1 ** (1/2))
                        
                    else:
                        raise ValueError("Not enough operands for operation")
                    
                else:
                    raise ValueError(f"Unknown token: {token}") 

        self.stack = stack  
        return stack

        
    def get_result(self):
        if not self.stack:
            return "No result"
        
        result = self.stack[-1]
        return int(result) if result.is_integer() else result
        



    

    