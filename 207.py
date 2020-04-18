class Solution:
    """
    BFS, 广度优先遍历；
    建立入度表和邻接表。
    """
    def canFinish(self, numCourses: int, prerequisites: list) -> bool:
        indegree = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]

        for cur, pre in prerequisites:
            indegree[cur] += 1
            adjacency[pre].append(cur)

        queue = []
        for cur in range(numCourses):
            if indegree[cur]==0:
                queue.append(cur)

        while queue:
            pre = queue.pop(0)
            numCourses -= 1
            for cur in adjacency[pre]:
                indegree[cur] -= 1
                if indegree[cur]==0:
                    queue.append(cur)
        return numCourses == 0
