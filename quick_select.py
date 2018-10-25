def kth_biggest(k, nums, begin, end):
    while k <= end - begin + 1:
        if end - begin == 0:
            return nums[begin];
        elif k == end - begin + 1:
            temp = nums[begin:end+1]
            temp.sort()
            return temp[0];
        else:
            pivot = nums[begin];
            head = begin;
            rear = end;
            while head!= rear:
                for i in xrange(head,rear + 1):
                    head = i;
                    if nums[head] > pivot:
                        break
                for j in xrange(rear, head-1, -1):
                    rear = j;
                    if nums[rear] <= pivot:
                        swap(nums, head, rear)
                        break
            if nums[head] > pivot:
                swap(l, head-1, begin);
            else:
                swap(l, head, begin);
            if end-head > k-1:
                return kth_biggest(k,nums,head+1,end);
            else:
                return kth_biggest(k-end+head, nums, begin, head)
    return


def swap(l, p1, p2):
    temp = l[p1];
    l[p1] = l[p2];
    l[p2] = temp;
    return


l = [9,3,2,4,8,1,33,54,44];
print (kth_biggest(1,l, 0, len(l)-1));