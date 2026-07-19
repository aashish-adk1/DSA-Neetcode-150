class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap={}
        index=0
        for num in nums:
            if num in hashmap:
                return True
            else:
                hashmap[num]=index
                index+=1
        return False