class Solution:
    def check(self, nums: List[int]) -> bool:
        size = len(nums)

        if size <= 1:
            return True

        inversion = 0

        if nums[0] < nums[size - 1]:
            inversion += 1

        for i in range(1, size):
            if nums[i] < nums[i - 1]:
                inversion += 1

        if inversion <= 1:
            return True
        return False
