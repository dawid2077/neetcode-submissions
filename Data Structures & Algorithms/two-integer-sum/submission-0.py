class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary={}
        for i,j in enumerate(nums):
            left=target-j
            if j in dictionary:
                return [dictionary[j],i]
            dictionary[left]=i
