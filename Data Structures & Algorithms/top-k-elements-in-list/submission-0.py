from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted=dict(Counter(nums))
        print(counted)
        #sort it 
        sorted_count = dict(
            sorted(counted.items(), key=lambda item: item[1], reverse=True)
        )
        sorted_count=list(sorted_count)
        return sorted_count[:k]