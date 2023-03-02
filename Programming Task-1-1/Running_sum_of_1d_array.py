class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        retList = [nums[0]]
        for i in range(1, len(nums)):
            retList.append(retList[-1]+nums[i])
        return retList
