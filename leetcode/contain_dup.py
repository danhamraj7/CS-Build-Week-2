class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        dup_val = set()
        for i in nums:
            if i in dup_val:
                return True
            else:
                dup_val.add(i)
        return False
