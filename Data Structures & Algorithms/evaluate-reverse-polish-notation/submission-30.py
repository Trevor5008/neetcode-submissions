import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        stack = []
        for val in tokens:
            if val not in operators:
                stack.append(val)
            else:
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                stack.append(int(operators[val](val1, val2)))
        return int(stack[0])