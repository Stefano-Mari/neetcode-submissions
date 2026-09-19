from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = Counter(nums) # O(n)

        buckets = [[] for _ in range(len(nums) + 1)] # O(n)

        for number, count in counts.items(): # O(d)
            buckets[count].append(number)

        result = []

        for i in range(len(buckets) - 1, 0, -1): # O(n)
            for number in buckets[i]: # O(d)
                result.append(number)

                if len(result) == k:
                    return result

    # O(n) + O(n) + O(n) + O(n) + O(d) = O(n), since d <= n
        