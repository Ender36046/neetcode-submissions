

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokens.reverse()
        operands = []
        operators = {'+','-','/','*'}

        while(len(tokens) > 0):
            token = tokens.pop()
            if(token in operators):
                operand2 = operands.pop()
                operand1 = operands.pop()
                if(token == '+'):
                    operands.append(operand1 + operand2)
                elif(token == '-'):
                    operands.append(operand1 - operand2)
                elif(token == '/'):
                    operands.append(math.trunc(operand1/operand2))
                elif(token == '*'):
                    operands.append(operand1*operand2)
            else:
                operands.append(int(token))
        return operands[0]

        