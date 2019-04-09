class Solution:
    def dfs(self, node, current_path):
        current_path = current_path + [node]
        for child in self.graph[node]:
            if child == len(self.graph) - 1:
                self.paths.append(current_path + [len(self.graph) - 1])
                continue
            self.dfs(child, current_path)
            
            
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.paths = []
        self.graph = graph

        if not graph:
            return []

        self.dfs(0, [])

        return self.paths
