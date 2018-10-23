#class Solution:
"""
@param n: An integer
@param nums: An array
@return: the Kth largest element
"""


def swap(l, j, k):
    temp = l[j]
    l[j] = l[k]
    l[k] = temp
    return l


def quickSort( l, begin, end):
    while end - begin > 0:
        pivot = l[begin];
        if end - begin == 1:
            if l[begin] > l[end]:
                swap(l, begin, end);
            # len(sublist) >= 3
        else:
            head = begin + 1;
            rear = end;
            while head < rear:
                while head < rear:
                    if l[head] <= pivot:
                        head = head + 1;
                    else:
                        break
                while head < rear:
                    if l[rear]> pivot:
                        rear -=1;
                    else:
                        break
                swap(l,head,rear);
            # return quickSort(l,head,)
            quickSort(l, begin, head-1);
            quickSort(l, head, end);
    return


def kthLargestElement( n, nums):
    # write your code here
    quickSort( nums, 0, len(nums)-1);
    print(nums[n]);


nums = [45, 45,66, 12, 3, 99]
kthLargestElement( 1, nums)
