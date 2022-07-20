class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(bums, l,m,h):
            total,j = 0,m+1
            for i in range(l,m+1):
                while j<=h and nums[i] > 2*nums[j]:
                    j += 1
                total += j-(m+1)
            left, right = l,m+1
            t = []
            while left<=m and right<=h:
                if nums[left] <= nums[right]:
                    t.append(nums[left])
                    left += 1
                else: 
                    t.append(nums[right])
                    right += 1
            while left<=m:
                t.append(nums[left])
                left += 1
            while right<=h:
                t.append(nums[right])
                right += 1
            for i in range(l,h+1):
                nums[i] = t[i-l]
            return total
        
        def mergesort(nums, l, r):
            c = 0
            if l<r:
                m = (l+r)//2
                c += mergesort(nums, l, m)
                c += mergesort(nums, m+1, r)
                c += merge(nums, l,m,r)
            return c
        
        return mergesort(nums,0,len(nums)-1)