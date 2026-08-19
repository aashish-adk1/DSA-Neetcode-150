class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        n = len(nums)
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        sorted_arr = [[] for _ in range(n + 1)]

        for key, value in hashmap.items():
            sorted_arr[value].append(key)

        output_arr = []

        for i in range(len(sorted_arr) - 1, -1, -1):
            if len(output_arr) >= k:
                break
            current_subarr=sorted_arr[i]
            for item in current_subarr:
                output_arr.append(item)
        
        return output_arr
