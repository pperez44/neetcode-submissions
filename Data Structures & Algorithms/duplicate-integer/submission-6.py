class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #hash set instantiation
        hashSet = set()
        for i in nums:
            if i in hashSet:
                return True
            hashSet.add(i)
        return False