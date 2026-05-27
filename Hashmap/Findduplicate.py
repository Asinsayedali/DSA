class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for value in nums:
            if value not in count:
                count[value] = 1
            else:
                count[value]+=1
        for key, value in count.items():
            if value >= 2:
                return True
        return False
        