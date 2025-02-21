

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        found = set()
        for num in nums:
            if num in found:
                return True
            found.add(num)
        return False

    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        found = {}
        for index, num in enumerate(nums):
            if num in found:
                if index - found[num] <= k:
                    return True
            found[num] = index
        return False
        


if __name__ == "__main__":
    testContDupes = Solution()

    if testContDupes.containsDuplicate([1,2,3,1]) == True:
        print("Testcase1: Passed")
    else:
        print("Testcase1: Failed")
    
    if testContDupes.containsDuplicate([1,2,3,4]) == False:
        print("Testcase2: Passed")
    else:
        print("Testcase2: Failed")
    
    if testContDupes.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True:
        print("Testcase3: Passed")
    else:
        print("Testcase3: Failed")


    if testContDupes.containsNearbyDuplicate([1,2,3,1],3) == True:
        print("Testcase1: Passed")
    else:
        print("Testcase1: Failed")
    
    if testContDupes.containsNearbyDuplicate([1,0,1,1],1) == True:
        print("Testcase2: Passed")
    else:
        print("Testcase2: Failed")
    
    if testContDupes.containsNearbyDuplicate([1,2,3,1,2,3],2) == False:
        print("Testcase3: Passed")
    else:
        print("Testcase3: Failed")

