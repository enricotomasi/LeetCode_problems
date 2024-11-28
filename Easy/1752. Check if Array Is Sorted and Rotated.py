class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
 
        n = len(nums)
        
        for i in range(n):
            last = nums[i]
            ok = True
            for j in range(n):
                pos = (j + i) %n
                
                if last > nums[pos]:
                    ok = False
                    break

                last = nums[pos]
            
            if ok:
                return True
        
        return False
