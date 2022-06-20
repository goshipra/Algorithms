class Solution(object):
    def singleNumber(self, nums):
        length = len(nums)
        if length == 1:
            return nums[0]

        if length % 2 == 0:
            return "Invalid Output"

        if length == 3:
            first_element = nums[0]
            if first_element in nums[1:]:
                nums.remove(first_element)
                nums.remove(first_element)
                first_element = nums[0]
                return first_element

        i = 0
        for element in nums[0:-2]:
            first_element = nums[i]
            if first_element in nums[1:]:
                nums.remove(first_element)
                nums.remove(first_element)
            else:
                first_element = nums[0]
                return first_element

arr = [2,2,1]
obj = Solution()
print(obj.singleNumber(arr))
