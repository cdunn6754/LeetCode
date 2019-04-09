class Solution:
    def dfs(self, node):
        if node == len(self.graph) - 1:
            return [[node]]
        if node in self.memo:
            return self.memo[node]
        
        paths = []
        for nei in self.graph[node]:
            for path in self.dfs(nei):
                paths.append([node] + path)

        self.memo[node] = paths
        return paths
                
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []
        self.graph = graph
        self.memo = {}

        return self.dfs(0)
        

        

