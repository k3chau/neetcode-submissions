import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+':operator.add, '-':operator.sub, 
        '*':operator.mul, '/':lambda a,b: int(a/b)}
        for token in tokens:
            if token in operators:
                right_operand = stack.pop()
                left_operand = stack.pop()
                result = operators[token](left_operand,right_operand)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[-1] if stack else -1 

        