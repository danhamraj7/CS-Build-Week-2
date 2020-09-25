class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}

        for i in range(len(nums)):
            match = target - nums[i]

            if match in dictionary:
                return [dictionary[match], i]

            dictionary[nums[i]] = i
