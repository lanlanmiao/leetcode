# -*-coding:utf-8 -*-
__author__ = 'guoxuemin'
class Solution(object):

    def function(self,root,res):
        if not root.children:
            res.append(root.val)
            return
        for child in root.children:
            self.function(child,res)

    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res=[]
        self.function(root,res)
        return res
solution=Solution()
root={"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}
ans=solution.postorder(root)
print ans