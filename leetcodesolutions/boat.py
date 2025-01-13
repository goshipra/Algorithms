# You are given an array people where people[i] is the weight of the ith person, and an
# infinite number of boats where each boat can carry a maximum weight of limit.
# Each boat carries at most two people at the same time, provided the sum of the weight
# of those people is at most limit.
# Return the minimum number of boats to carry every given person.

class Solution(object):
    '''
    Rescue boat algorithm which has limit of max weight of people
    and number of people to be rescued.
    '''
    def numRescueBoats(self, people, limit):
        people.sort()
        left,right = 0,len(people)-1
        count = 0
        while left <= right:
            if (people[right] + people[left]) <= limit:
                count += 1
                left = left + 1
                right = right -1
            else:
                count += 1
                right = right -1

        return count


    # def numRescueBoats(self, people, limit):
    #     people.sort()
    #     left = 0
    #     right = len(people) - 1
    #     count = 0
    #
    #     while left <= right:
    #         remaining = limit - people[right]
    #         if left <= right and remaining >= people[left]:
    #             left += 1
    #         right -= 1
    #         count += 1
    #
    #     return count




# Main Program
people = [1,2,2,3]
min_boats = Solution()
print(min_boats.numRescueBoats(people, limit=3))
