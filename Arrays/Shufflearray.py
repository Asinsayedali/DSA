class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = nums[:n]
        insert_pos = 1
        for i in range(n,2*n):
            result.insert(insert_pos, nums[i])
            insert_pos+=2
        return result