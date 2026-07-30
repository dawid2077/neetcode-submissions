class MinStack:

    def __init__(self):
        self.list=[]
        self.minlist=[]
    def push(self, val: int) -> None:
        self.list.append(val)
        try:
            if val<=self.minlist[-1]:
                self.minlist.append(val)
        except:
            self.minlist.append(val)
            
            

    def pop(self) -> None:
        if self.list[-1]==self.minlist[-1] and len(self.minlist)!=1:
            self.minlist.pop()
        self.list.pop()


    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        print(self.minlist)
        return self.minlist[-1]
        
