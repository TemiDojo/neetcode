class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i,j in enumerate(strs):
            res += str(len(j)) + "#"
            res += j
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        tmp = ""
        count = 0
        while i < len(s):
            print(i)
            if s[i].isdigit():
                tmp += s[i]
                i+=1
                continue
            elif s[i] == '#':
                count = int(tmp)
                tmp = ""
                i += 1
            res.append(s[i:count+i])
            i += (count)
        return res
