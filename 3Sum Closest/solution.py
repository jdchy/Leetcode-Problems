def threeSumClosest(nums,target):
    nums.sort() 
    answer = nums[0] + nums[1] + nums[2]

    for i in range(len(nums)-2):
        j=i+1
        k=len(nums)-1
        while(j<k):
            total=nums[i]+nums[j]+nums[k]
            print(total,i,j,k)
            if total < target: 
                j=j+1
            elif total > target:  
                k=k-1
            else:
                return total
            if abs(total - target) < abs(answer - target):
                answer = total
            print(answer)
    return answer

if __name__ == '__main__':
    threeSumClosest([-1,2,1,-4],1)
            