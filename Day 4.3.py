def smallernumberthancurrent(nums):
    count=[0]*len(nums)
    for i in range (len(nums)):
        for j in range(len(nums)):
            if nums[j]<nums[i]:
                count[i]+=1
    return count
print(smallernumberthancurrent([8,1,2,2,3]))
