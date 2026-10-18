import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        res = []
        for token in tokens:
            if token not in operators:
                res.append(int(token))
            else:
                val2 = int(res.pop())
                val1 = int(res.pop())
                res.append(int(operators[token](val1, val2)))
        return res[0]