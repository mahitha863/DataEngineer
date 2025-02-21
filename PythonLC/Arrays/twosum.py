

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        testMap = {}
        for index, num in enumerate(nums):
            if target-num in testMap:
                return [testMap[target-num], index]
            testMap[num] = index

        return []


if __name__ == "__main__":
    test2sum = Solution()

    if test2sum.twoSum([2,7,11,15], 9) == [0,1]:
        print("Testcase1: Passed")
    else:
        print("Testcase1: Failed")
    
    if test2sum.twoSum([3,2,4], 6) == [1,2]:
        print("Testcase2: Passed")
    else:
        print("Testcase2: Failed")
    
    if test2sum.twoSum([3,3], 6) == [0,1]:
        print("Testcase3: Passed")
    else:
        print("Testcase3: Failed")

