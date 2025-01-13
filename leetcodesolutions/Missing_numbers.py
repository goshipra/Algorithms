
class Solution(object):
    '''
    Finding missing number from a range
    '''
    def missingNumber(self, nums):

        if len(nums) < 2:
            if len(nums) == 0:
                return False
            if nums[0] == 1:
                return 0
            if nums[0] == 0:
                return 1


        nums.sort()
        missing = nums[-1] + 1
        if nums[0] != 0:
            return 0
        else:
            for i in range(len(nums)-1):
                if nums[i] + 1 == nums[i+1]:
                    continue
                else:
                    return nums[i] + 1

        return missing

    # def missingNumber(self, nums):
    #
    #     nums.sort()
    #     n = len(nums) + 1
    #     value = 0
    #     min_element = nums[0]
    #     max_element = nums[-1]
    #
    #     if min_element != 0:
    #         return value
    #
    #
    #     for i in range (min_element,max_element):
    #         if i in nums:
    #             continue
    #         else:
    #             value = i
    #     if value == 0:
    #         value = max_element + 1
    #
    #     return value


arr = [0,2,3]
obj = Solution()
print(obj.missingNumber(arr))