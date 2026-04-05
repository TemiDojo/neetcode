class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # create an array ans of length 2n : ans[i] == nums[i] && ans[i + n] == nums[i]
        ans = []
        i = 0
        j = 0
        
    
        while i < 2:
            
            ans.insert(j, nums[j])
            j = j + 1

            if j % len(nums) == 0:
                i = i + 1
                j = 0
        return ans
            