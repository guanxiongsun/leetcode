def kth_biggest(k, nums, begin, end):
    while k <= end - begin + 1:
        if end - begin == 0:
            return nums[begin];
        elif 1 == end - begin:
            temp = nums[begin:end+1]
            temp.sort()
            return temp[2-k];
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
                swap(nums, head-1, begin);
                if end - head + 1 == k-1:
                    return pivot;
                elif end - head + 1 > k-1:
                    return kth_biggest(k, nums, head, end);
                else:
                    return kth_biggest(k - end + head - 1, nums, begin, head-1)
            else:
                swap(nums, head, begin);
                if end - head == k-1:
                    return pivot;
                elif end - head > k-1:
                    return kth_biggest(k, nums, head+1, end);
                else:
                    return kth_biggest(k - end + head, nums, begin, head)
    return


def swap(l, p1, p2):
    temp = l[p1];
    l[p1] = l[p2];
    l[p2] = temp;
    return


ll = [1,3,4,2]
print (kth_biggest(1, ll, 0, len(ll)-1))