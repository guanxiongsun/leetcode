# class Solution:
"""
@param n: An integer
@param nums: An array
@return: the Kth largest element
"""


def swap(l, j, k):
    temp = l[j]
    l[j] = l[k]
    l[k] = temp
    return


def quick_sort(l, begin, end):
    if end-begin < 1:
        return
    elif end-begin ==1:
        if l[begin] > l[end]:
            swap(l, begin, end)
        else:
            return
    else:
        # length of l >= 3
        pivot = l[begin];
        head = begin;
        rear = end;
        while head != rear:
            for i in xrange(head, rear+1):
                head = i
                if l[head] > pivot:
                    break
            if head != rear:
                for j in xrange(rear, head-1, -1):
                    rear = j
                    if l[rear] <= pivot:
                        swap(l, head, rear)
                        break
        if l[head] <= pivot:
            swap(l, begin, head)
        else:
            swap(l, begin, head-1)
        quick_sort(l, begin, head-1)
        quick_sort(l, head+1, end)
    return


def kthLargestElement(n, nums):
    # write your code here
    quick_sort(nums, 0, len(nums)-1);
    print(nums[n]);


my_nums = [45, 45, 66, 12, 3, 99]
kthLargestElement(1, my_nums)
