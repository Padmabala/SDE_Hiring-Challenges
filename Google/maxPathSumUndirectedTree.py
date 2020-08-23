from collections import defaultdict
class Solution(object):
    def sumOfDistancesInTree(self, N, values, edges):
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        def findMaxSum(node,parent):
            i=0
            childSumAsBranch=[]
            childMaxPathSum=[]
            for child in graph[node]:
                if(child!=parent):
                    csb,cps=findMaxSum(child,node)
                    childSumAsBranch.append(csb)
                    childMaxPathSum.append(cps)
                    i+=1
                else:
                    continue
            currentRoot=values[node-1]
            maxAmongChildSumAsBranch=float('-inf')
            for c in childSumAsBranch:
                maxAmongChildSumAsBranch=max(maxAmongChildSumAsBranch,c)
            maxSumAsBranch=max(maxAmongChildSumAsBranch+currentRoot,currentRoot)
            sumOfAllChild=0
            for c in childSumAsBranch:
                sumOfAllChild+=c
            maxSumAsRootNode=max(sumOfAllChild+currentRoot,maxSumAsBranch)
            maxAmongChildMaxPathSum=float('-inf')
            for c in childMaxPathSum:
                maxAmongChildMaxPathSum=max(maxAmongChildMaxPathSum,c)
            maxPathSum=max(maxAmongChildMaxPathSum,maxSumAsRootNode)
            return (maxSumAsBranch,maxPathSum)

        _, maxSum = findMaxSum(1, None)
        return maxSum

n=7
values=[6,3,10,-9,-4,-8,-6]
# edges=[[0,1],[0,2]]
edges=[[6,5],[7,2],[3,5],[2,1],[5,7],[4,3]]
s=Solution()
print(s.sumOfDistancesInTree(n,values,edges))
