class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        ret = []
        for i, j in enumerate(nums):
            if j not in m:
                s = set()
                s.add(i)
                m[j] = s
            else:
                m[j].add(i)
        print(m)
        for i, j in enumerate(nums):
            res = target -j
            if res in m:
                a = 0
                b = 0
                if len(m[res]) == 1 and i not in m[res]:
                    a = m[res].pop()
                    b = i
                
                elif len(m[res]) > 1:
                    print("hello")
                    a = m[res].pop()
                    b = m[res].pop()
                else:
                    continue

                if a <= b:
                    ret.append(a)
                    ret.append(b)
                else:
                    ret.append(b)
                    ret.append(a)
                               
                break
            
        return ret