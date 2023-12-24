def twoSum(self, nums, target):
    nums1 = {}
    for i in range(len(nums)):
        if nums1.get(nums[i], -1) != -1:
            return [i, nums1[nums[i]]]
        nums1[target-nums[i]] = i

