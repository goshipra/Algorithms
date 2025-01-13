# Mountain array

class Solution(object):
    '''
    Find out the given array is mountain array aor not
    '''

    def validMountainArray(self, arr):

        if len(arr) < 3:
            return False
        i = 0
        max = 0
        while i < len(arr) - 1:
            if arr[i] < arr[i+1]:
                max = arr[i+1]
                i += 1
                continue
            else:
                break

        if max == 0:
            return False
        print("max : ", max)

        i = arr.index(max)
        if i == len(arr)-1:
            return False
        min = max
        while i < len(arr)-1:
            if arr[i] > arr[i+1]:
                min = arr[i+1]
                i += 1
            else:
                return False
        return True


    #
    # def validMountainArray(self, arr):
    #
    #     if len(arr) < 3:
    #         return False
    #
    #     max_element = max(arr)
    #     index_max_element = arr.index(max_element)
    #     last_element = arr[-1]
    #     first_element = arr[0]
    #     if index_max_element == arr.index(last_element) or index_max_element == arr.index(first_element):
    #         return False
    #
    #     left_list = arr[:index_max_element+1]
    #     right_list = arr[index_max_element:]
    #
    #     length_left = len(left_list) - 1
    #     i = 0
    #     while i < length_left:
    #         if left_list[i] < left_list[i+1]:
    #             i += 1
    #         else:
    #             return False
    #
    #     length_right = len(right_list)-1
    #     j = 0
    #     while j < length_right:
    #         if right_list[j] > right_list [j+1]:
    #             j += 1
    #         else:
    #             return False
    #
    #     return True


arr = [1,2,3,4,5,6,7]
obj = Solution()
print(obj.validMountainArray(arr))
