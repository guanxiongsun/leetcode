class Solution:
    """
    @param length: the length of the array
    @param updates: update operations
    @return: the modified array after all k operations were executed
    """
    # 暴力解法 TLE
    # def getModifiedArray(self, length, updates):
    #     # Write your code here
    #     answer = [0 for _ in range(length)]
    #     for update in updates:
    #         self.range_addition(answer, update[0], update[1], update[2])
    #     return answer
    #
    # def range_addition(self, l, start, end, increase):
    #     for x in range(start, end+1):
    #         l[x] = l[x] + increase
    #     return l

    # 在start 位置记录val
    # 在end+1 位置记录-val
    # 相当于记录pivot在每个位置的增量
    # 在遍历过程中用记录的值动态更新pivot
    def getModifiedArray(self, length, updates):
        # Write your code here
        answer = [0 for _ in range(length+1)]
        for update in updates:
            answer[update[0]] += update[2]
            answer[update[1]+1] -= update[2]
        pivot = 0
        for index in range(length):
            pivot += answer[index]
            answer[index] = pivot
        return answer[:-1]
