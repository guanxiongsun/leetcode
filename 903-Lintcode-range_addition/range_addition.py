class Solution:
    """
    @param length: the length of the array
    @param updates: update operations
    @return: the modified array after all k operations were executed
    """
    def getModifiedArray(self, length, updates):
        # Write your code here
        answer = [0 for _ in range(length)]
        for update in updates:
            self.range_addition(answer, update[0], update[1], update[2])
        return answer

    def range_addition(self, l, start, end, increase):
        for x in range(start, end+1):
            l[x] = l[x] + increase
        return l
