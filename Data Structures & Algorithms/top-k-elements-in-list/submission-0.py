class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        output = []

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        while k > 0:
            max_val = max(counts, key=counts.get)
            output.append(max_val)
            del counts[max_val]
            k -= 1

        return output