def kth_biggest(k, nums):

    temp = nums[0:k];
    temp.sort();

    for i in nums:
        if i >= temp[0]:
            temp[0] = i;
            temp.sort();

    return temp[0]

l = [9,3,2,4,8];
print (kth_biggest(3,l));