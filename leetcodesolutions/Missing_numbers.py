
class Solution(object):
    '''
    Finding missing number from a range
    '''
    def missingNumber(self, nums):

        nums.sort()
        n = len(nums) + 1
        value = 0
        min_element = nums[0]
        max_element = nums[-1]

        if min_element != 0:
            return value


        for i in range (min_element,max_element):
            if i in nums:
                continue
            else:
                value = i
        if value == 0:
            value = max_element + 1

        return value


arr = [0]
obj = Solution()
print(obj.missingNumber(arr))