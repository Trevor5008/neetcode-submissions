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
                val1 = int(res.pop())
                val2 = int(res.pop())
                res.append(int(operators[token](val2, val1)))
        return res[0]