# @lcpr-before-debug-begin
from python3problem219 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=219 lang=python3
# @lcpr version=30204
#
# [219] 存在重复元素 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict
class Solution:
    # def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    #     groups = defaultdict(list)
    #     for i, num in enumerate(nums):
    #         groups[num].append(i)
        
        
    #     for v in groups.values():
    #         for index in range(1, len(v)):
    #             if v[index] - v[index - 1] <= k:
    #                 return True
        
    #     return False
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last = {}
        for i, num in enumerate(nums):
            if num in last and i - last[num] <= k:
                return True
            last[num] = i
        return False

# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1,2,3]\n2\n
# @lcpr case=end

#

