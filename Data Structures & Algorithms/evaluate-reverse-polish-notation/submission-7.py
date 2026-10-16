import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b)
        }
        stack = []
        for char in tokens:
            if char not in operators:
                stack.append(int(char))
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                op_func = operators.get(char)
                stack.append(op_func(val2, val1))
        return int(stack[0])