class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for i in nums:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1
            
        res = []
        for i in range(0, k):
            max = 0
            val = -1000
            for j in m:
                if m[j] > max:
                    max = m[j]
                    val = j

            res.append(val)
            m.pop(val, None)
        return res