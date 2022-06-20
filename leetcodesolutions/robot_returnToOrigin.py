class Solution(object):
    def judgeCircle(self, moves):
        count = 0

        for char in moves:
            if char == 'R':
                count += 4
            elif char == 'L':
                count -= 4
            elif char == 'U':
                count += 5
            elif char == 'D':
                count -= 5
            else:
                return False

        if count == 0:
            return True
        else:
            return False


string = 'ULL'
obj = Solution()
print(obj.judgeCircle(string))