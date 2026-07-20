class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(len(nums)):
            remainder=target-nums[i]
            if remainder in hashmap:
                if i<hashmap[remainder]:
                    return [i,hashmap[remainder]]
                return [hashmap[remainder],i]
            hashmap[nums[i]]=i
        return [-1,-1]