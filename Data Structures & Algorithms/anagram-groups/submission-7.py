class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # we need a seen set
        m = defaultdict(list)
        for i in strs:
            arr = [0] * 26
            for j in i:
                arr[ord(j) - ord('a')] += 1
            m[tuple(arr)].append(i)
        
        return list(m.values())