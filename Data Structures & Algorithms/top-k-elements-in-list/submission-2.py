from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for number, count in counts.items():
            buckets[count].append(number)

        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for number in buckets[i]:
                result.append(number)

                if len(result) == k:
                    return result
        