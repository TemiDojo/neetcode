class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, j in enumerate(nums):
            diff = target - j
            if diff in m:
                return [m[diff], i]
            m[j] = i
        return []