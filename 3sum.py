class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result_set = set()
        n = len(nums)
        
        for i in range(n - 2):
            left, right = i + 1, n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result_set.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return [list(triplet) for triplet in result_set]