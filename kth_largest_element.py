class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def swap(l, j, k):
        temp = l(j);
        l(j) = l(k);
        l(k) = temp;

    def quickSort ( l , begin, end):
        while end - begin > 1:
            pivot = l(begin);
            if end - begin == 2:
                if l(begin)>l(end):
                    swap(l,begin,end);
                # len(sublist) >= 3
                else:
                    head = begin + 1;
                    rear = end;
                    while head < rear:
                        while head < rear:
                            while l(head)<=pivot:
                                head +=1;
                        while head < rear:
                            while l(rear)> pivot:
                                rear -=1;
                        swap(l,head,rear);
                # return quickSort(l,head,)
                quickSort(l, begin, head-1);
                quickSort(l, head, end);
        return

    def kthLargestElement(self, n, nums):
        # write your code here
        quickSort(nums);
        print(nums(n));
