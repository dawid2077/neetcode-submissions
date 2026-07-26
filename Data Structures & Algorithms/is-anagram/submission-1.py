class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        encoding = {
            'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 
            'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 
            'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 
            'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 
            'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 
            'z': 101
        }
        num1=1
        num2=1
        for l,l2 in zip(s,t):
            num1=num1*encoding[l]
            num2=num2*encoding[l2]
        if num1==num2:
            return True
        else:
            return False
