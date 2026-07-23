class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        arr=[]
        for s in strs:
            sorted_s= "".join(sorted(s))
            hashmap.setdefault(sorted_s,[]).append(s)

        for value in hashmap.values():
            arr.append(value)
        return arr
        
