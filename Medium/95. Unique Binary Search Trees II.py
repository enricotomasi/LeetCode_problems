# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def rec(start, end):
            if start > end:
                return [None]
            
            ans = []
            
            for i in range(start, end + 1):
                for j in rec(start, i - 1):
                    for k in rec(i + 1, end):
                        temp = TreeNode(i)
                        temp.left = j
                        temp.right = k
                        ans.append(temp)
                        
            return ans
        
        return rec(1, n)