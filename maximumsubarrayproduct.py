def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        ans=nums[0]
        maximum=[1]*n
        minimum=[1]*n
        maximum[0]=ans
        minimum[0]=ans
        for i in range(1,n):
            if nums[i]==0:
                maximum[i]=0
                minimum[i]=0
            else:
                maximum[i]=max(nums[i],minimum[i-1]*nums[i],maximum[i-1]*nums[i])
                minimum[i]=min(nums[i],minimum[i-1]*nums[i],maximum[i-1]*nums[i])
            ans=max(ans,maximum[i])
        return ans
