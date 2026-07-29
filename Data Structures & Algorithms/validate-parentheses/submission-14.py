class Solution:
    def isValid(self, s: str) -> bool:
        toClose=[]
        left=["[","{","("]
        right=["]","}",")"]
        reverse = {
            '[': ']',
            ']': '[',
            '(': ')',
            ')': '(',
            '{': '}',
            '}': '{',
        }
        if len(s)==1:
            return False
        for i in s:
            if i in left:
                toClose.append(i)
            if i in right:
                try:
                    if reverse[i]==toClose[-1]:
                        toClose.pop()
                    else:
                        return False
                except:
                    return False
        if len(toClose)==0:
            return True
        else:
            return False


