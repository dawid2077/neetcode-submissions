from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=deque()
        operations={"+","-","*","/"}

        for i in tokens:
            stack.append(i)
            if i in operations:
                op=stack[-1]
                #print(op)
                stack.pop()
                num1=stack[-1]
                stack.pop()
                #print(num1)
                num2=stack[-1]
                stack.pop()
                #print(num2)
                num1=int(num1)
                num2=int(num2)
                num3=0
                match op:
                    case "+":
                        num3=num1+num2
                    case "-":
                        num3=num2-num1
                    case "*":
                        num3=num1*num2
                    case "/":
                        num3=num2/num1
                #print(num3)
                stack.append(num3)
        return int(stack[-1])




        