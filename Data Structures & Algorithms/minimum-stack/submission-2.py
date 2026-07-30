class MinStack:

    def __init__(self):
        self.list=[]
        self.minlist={} #{len(list)->min_value}
    def push(self, val: int) -> None:
        if len(self.minlist)==0:
            self.minlist[0]=val
        else:
            #print(self.minlist)
            self.new_pos=len(self.list)
            self.old_pos=len(self.list)-1
            #print(self.new_pos)
            #print(self.old_pos)
            if len(self.list)!=0:
                self.minlist[self.new_pos]=self.minlist[self.old_pos]
                if val <= self.minlist[len(self.list)]:
                    self.minlist[len(self.list)]=val
        self.list.append(val)
        #print(self.minlist)

            
            

    def pop(self) -> None:
        #if self.list[-1]==self.minlist[len(self.list)-1] and len(self.minlist)!=1:
        if True==True:
            #in future we will have to clean old values
            if len(self.list)!=1:
                self.minlist.pop(len(self.minlist)-1)
                self.list.pop()
            else:
                self.list=[]
                self.minlist={}
                print("last item")
        #print(self.minlist)


    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        #print(self.minlist)
        return self.minlist[len(self.list)-1]
        

# 3,-2,5,-8 

