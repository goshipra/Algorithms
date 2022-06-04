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
        count = 0
        index = 0
        length = len(people) - 1

        people.sort()

        while index <= length:
            remain = limit - people[length]

            length -= 1
            if people[index] <= remain:
                index += 1
            count += 1

        return count


# Main Program
people = [2,2,1]
min_boats = Solution()
print(min_boats.numRescueBoats(people, limit=5))
