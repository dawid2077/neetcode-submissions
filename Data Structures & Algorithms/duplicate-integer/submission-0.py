class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set={""}
        for number in nums:
            if number in set:
                return True
            set.add(number)
        return False
            
