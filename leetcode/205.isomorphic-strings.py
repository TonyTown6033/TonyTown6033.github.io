# @lcpr-before-debug-begin
from python3problem205 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=205 lang=python3
# @lcpr version=30204
#
# [205] 同构字符串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict
class Solution:
    # def isIsomorphic(self, s: str, t: str) -> bool:
    #     sGroup = defaultdict(list)
    #     for i, c in enumerate(s):
    #         sGroup[c].append(i)
        
    #     tGroup = defaultdict(list)
    #     for i, c in enumerate(t):
    #         tGroup[c].append(i)
        
    #     return list(sGroup.values()) == list(tGroup.values())
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t = {}
        t2s = {}
        for (a, b) in zip(s,t):
            if a in s2t and s2t[a] != b:
                return False
            if b in t2s and t2s[b] != a:
                return False
            s2t[a] = b
            t2s[b] = a
        return True
# @lc code=end



#
# @lcpr case=start
# "egg"\n"add"\n
# @lcpr case=end

# @lcpr case=start
# "f11"\n"b23"\n
# @lcpr case=end

# @lcpr case=start
# "paper"\n"title"\n
# @lcpr case=end

#

