class Solution(object):
    def containsDuplicate(self, nums):
        nums2 = {}
        for num in nums:
            nums2[num] = True
        return len(nums2.values()) != len(nums)