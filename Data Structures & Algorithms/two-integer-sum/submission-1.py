class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, num in enumerate(nums):
            if hm.get(num) is not None:
                print(hm.get(num))
                return [hm.get(num),i]
            hm[target-num] = i
        print(hm)
        return []