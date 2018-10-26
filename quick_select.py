def kth_biggest(k, nums, begin, end):
    if k<0 or len(nums)<1 or begin>end or k>end-begin+1:
        return -1
    else:
        # k < end - begin + 1
        pivot = nums[begin];
        head = begin;
        rear = end;
        while head < rear:
            while nums[head] <= pivot and head < rear:
                head += 1
            while nums[rear] > pivot and head < rear:
                rear -= 1
            swap(nums, head, rear)
        # judge nums[head=rear] and pivot
        if nums[head] > pivot:
            num_bigger = end - head + 1
            if num_bigger == k-1:
                return pivot
            elif num_bigger > k-1:
                return kth_biggest(k, nums, head, end)
            else:
                return kth_biggest(k-num_bigger, nums, begin, head-1)
        else:
            swap(nums, begin, head)
            num_bigger = end - head
            if k == 1:
                return pivot
            if num_bigger == k-1:
                return pivot
            elif num_bigger > k-1:
                return kth_biggest(k, nums, head+1, end)
            else:
                return kth_biggest(k - num_bigger, nums, begin, head-1)
    return


def swap(l, p1, p2):
    temp = l[p1];
    l[p1] = l[p2];
    l[p2] = temp;
    return


ll = [1,1,1,1,1,13,4,2,999]
print (kth_biggest(3, ll, 0, len(ll)-1))