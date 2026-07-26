from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counted={}
        for i,word in enumerate(strs):
            print(Counter(word))
            temp=Counter(word)
            temp=dict(temp)
            temp=tuple(sorted(temp.items()))
            #in line below is an error cant use sorted nor tuple because it destroys the dictionary 
            print(temp)
            if temp in counted:
                counted[temp].append(i)
                #here we append if there is a duplicate
            else:
                counted[temp]=[i]
        print(counted)

        output=[]
        for count in counted:
            index=counted[count]
            mini_list=[]
            for x in index:
                originalWord=strs[x]
                mini_list.append(originalWord)
                print(originalWord)
            output.append(mini_list)
        return(output)
