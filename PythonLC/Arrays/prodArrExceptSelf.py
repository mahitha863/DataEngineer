

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        The idea is you can just prepare prefix array and postfix array and do product of it.
        But as we dont want 2 more extra space arrays, we put prefix array in result and 
        update it simultaneously doing postfix operation
        """
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix 
            prefix = prefix * nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]
        return res


if __name__ == "__main__":
    prodArr = Solution()

    if prodArr.productExceptSelf([1,2,3,4]) == [24,12,8,6]:
        print("Testcase1: Passed")
    else:
        print("Testcase1: Failed")
    
    if prodArr.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]:
        print("Testcase2: Passed")
    else:
        print("Testcase2: Failed")

