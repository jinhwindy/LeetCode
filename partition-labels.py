 class Solution(object):
    def partitionLabels(self, S):
        last = {char: ind for ind, char in enumerate(S)}
        # anchor 用于标记上个片段的结尾
        # j 用于
        j = anchor = 0
        ans = []
        for ind, char in enumerate(S):
            j = max(j, last[char])
            if ind == j:
                ans.append(ind - anchor + 1)
                anchor = ind + 1
            
        return ans
