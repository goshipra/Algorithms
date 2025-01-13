# Given an integer array nums, move all 0's to
# the end of it while maintaining the relative order
# of the non-zero elements.
# Note that you must do this in-place without making a
# copy of the array.

class Solution(object):
    def moveZeroes(self, nums):
        if len(nums) < 2:
            return nums

        left, right = 0, 1

        while right < len(nums):
            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
            elif nums[left] == 0 and nums[right] == 0:
                right += 1
            elif nums[left] != 0 and nums[right] == 0:
                left += 1
            elif nums[left] != 0 and nums[right] != 0:
                left += 1
                right += 1

        return nums



            # class Solution(object):
#     def moveZeroes(self, nums):
#         if len(nums) < 2:
#             return nums
#         i=0
#         for elements in nums:
#             if nums[i] == 0:
#                 nums.append(0)
#                 nums.remove(nums[i])
#             i+=1
#         return nums

arr = [0,1,0,3,12]
obj = Solution()
answer = obj.moveZeroes(arr)
print(answer)
