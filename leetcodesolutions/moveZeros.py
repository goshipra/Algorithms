# Given an integer array nums, move all 0's to
# the end of it while maintaining the relative order
# of the non-zero elements.
# Note that you must do this in-place without making a
# copy of the array.

class Solution(object):
    def moveZeroes(self, nums):
        if len(nums) < 2:
            return nums
        i=0
        j=-1

        lenght = (len(nums)//2)+1
        for elements in nums[:lenght]:
            if nums[i] == 0 and nums[j] == 0:
                j-=1
                nums[j],nums[i] = nums[i],nums[j]
                i+=1
            elif nums[i] == 0 and nums[j] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j-=1
            elif nums[i] !=0 and nums[j] != 0:
                i+=1


            print(nums)


class Solution(object):
    def moveZeroes(self, nums):
        if len(nums) < 2:
            return nums
        i=0
        for elements in nums:
            if nums[i] == 0:
                nums.append(0)
                nums.remove(nums[i])
            i+=1
        return nums

arr = [0,1,0,3,12]
obj = Solution()
answer = obj.moveZeroes(arr)
print(answer)
