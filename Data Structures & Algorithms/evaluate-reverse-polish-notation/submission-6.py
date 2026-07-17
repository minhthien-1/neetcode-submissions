class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if x in ["+","-","*","/"]:
                a = stack.pop()
                b = stack.pop()
                c = int(eval(f"{b}{x}{a}"))
                stack.append(c)
            else:
                stack.append(int(x))
        return stack[0]