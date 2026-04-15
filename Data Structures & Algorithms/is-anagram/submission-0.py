class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = defaultdict(list)

        if len(s) != len(t):
            return False
        arr = [0] * 26
        for i in s:
            arr[ord(i) - ord('a')] += 1
        m[tuple(arr)].append(s)
        arr = [0] * 26
        for i in t:
            arr[ord(i) - ord('a')] += 1
        m[tuple(arr)].append(t)

        print(m)
        if len(m) == 1:
            return True
        return False
