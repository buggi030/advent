class Solution:
    def nextPermutation(self, nums):
        print(nums)
        for i in range(len(nums)-1,-1,-1):
            if nums[i]> nums[i-1]:
                break
        if i > 0:
            indexToChange = i - 1
            for j in range(indexToChange+1, len(nums)):
                if nums[indexToChange] >= nums[j]:
                    nums[j-1], nums[i-1] = nums[i-1], nums[j-1]
                    print('a',nums)
                    break
                if j == len(nums)-1:
                    nums[j], nums[i-1] = nums[i-1], nums[j]
                    print('b',nums)

        left, right = i, len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1
        print(nums)

s = Solution()
s.nextPermutation([1, 5, 8, 4, 7, 6, 5, 3, 1])
s.nextPermutation([1,5,1])
