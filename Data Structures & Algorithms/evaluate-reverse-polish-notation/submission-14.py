import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        q = deque()
        res = []
        for token in tokens:
            if token not in operators:
                q.append(int(token))
            else:
                val1 = int(q.pop())
                val2 = int(q.pop())
                val = int(operators[token](val2, val1))
                q.append(val)
                    
        return q[0]