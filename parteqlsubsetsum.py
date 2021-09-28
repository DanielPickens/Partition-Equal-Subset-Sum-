def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_ % 2 == 1: return False
        self.dp = [-1 for j in range(sum_//2+1)]
        return self.__canPartition(nums, sum_//2, 0)
    def __canPartition(self, nums, target, idx):
        if idx == len(nums) or target < 0:
            return False
        if target - nums[idx] == 0:
            self.dp[target] = True
            return True
        if self.dp[target] != -1:
            return self.dp[target]
        can_partition = self.__canPartition(nums, target-nums[idx], idx+1) or self.__canPartition(nums, target, idx+1)
        self.dp[target] = can_partition
        return can_partition
      
      
      
      #Success
#Details 
#Runtime: 108 ms, faster than 95.02% of Python3 online submissions for Partition Equal Subset Sum.
#Memory Usage: 14.7 MB, less than 72.68% of Python3 online submissions for Partition Equal Subset Sum.
