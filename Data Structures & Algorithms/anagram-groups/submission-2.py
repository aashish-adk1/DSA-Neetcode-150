class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = defaultdict(list)

        for str in strs:
            count = [0]*26
            for i in range(len(str)):
                count[ord(str[i]) % ord('a')] += 1
            
            my_tuple = tuple( count )

            if my_tuple in hashtable: 
                hashtable[my_tuple].append(str)
            else:
                hashtable[my_tuple] = [str]
            
        return list(hashtable.values())
        
