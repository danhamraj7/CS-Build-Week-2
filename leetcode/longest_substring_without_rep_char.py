class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dictionary = {}
        left = 0
        right = 0
        ans = 0
        string = len(s)

        while(left < string and right < string):
            ele = s[right]
            if(ele in dictionary):
                left = max(left, dictionary[ele] + 1)

            dictionary[ele] = right
            ans = max(ans, right - left + 1)
            right += 1

        return ans
