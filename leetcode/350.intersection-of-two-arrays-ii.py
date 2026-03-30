#
# @lc app=leetcode.cn id=350 lang=python3
# @lcpr version=30204
#
# [350] 两个数组的交集 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        count = Counter(nums2)
        result = []
        for x in nums1:
            if x in count and count[x] > 0:
                result.append(x)
                count[x] -= 1
        return result
# @lc code=end



#
# @lcpr case=start
# [1,2,2,1]\n[2,2]\n
# @lcpr case=end

# @lcpr case=start
# [4,9,5]\n[9,4,9,8,4]\n
# @lcpr case=end

#

