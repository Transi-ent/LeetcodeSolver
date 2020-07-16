class Solution:
    """
    染色法：
    1. 对于节点 i, 其可达的节点有j, k, q, 则将节点i染成绿色，j, k, q 染成红色。
    因为节点i 可以与节点j,k ,q连成边，必须是不同的颜色。
    2. 遍历邻接表，当出现染色冲突时，说明不是二分图，否则就是；
    3. 使用深度优先搜索（使用BFS也可）；
    """
    def isBipartite(self, graph: list) -> bool:
        n = len(graph)
        UNCOLOR, RED, GREEN = 0, 1, 2
        valid = True
        colorMap = [UNCOLOR]*n

        def dfs(v: int, color: int):
            nonlocal valid
            colorMap[v] = color
            cNei = RED if color==GREEN else GREEN
            for neighbor in graph[v]:
                if colorMap[neighbor]==UNCOLOR:
                    dfs(neighbor, cNei)
                    if not valid:
                        return
                elif colorMap[neighbor]!=cNei:
                    valid = False
                    return

        for i in range(n):
            if colorMap[i]==UNCOLOR:
                dfs(i, GREEN)
            if not valid:
                break
        return valid



# g = [[],[10,44,62],[98],[59],[90],[],[31,59],[52,58],[],
#      [53],[1,63],[51,71],[18,64],[24,26,45,95],[61,67,96],[],
#      [40],[39,74,79],[12,21,72],[35,85],[86,88],[18,76],[71,80],
#      [27,58,85],[13,26,87],[75,94],[13,24,68,77,82],[23],[56,96],
#      [67],[56,73],[6],[41],[50,88,91,94],[],[19,72,92],[59],[49],
#      [49,89],[17],[16],[32,84,86],[61,73,77],[94,98],[1,74],
#      [13,57,90],[],[93],[],[37,38,54,68],[33],[11],[7,85],[9],
#      [49],[61],[28,30,87,93],[45,69,77],[7,23,76],[3,6,36,62],[81],
#      [14,42,55,62],[1,59,61],[10],[12,93],[],[96],[14,29,70,73],
#      [26,49,71,76],[57,83],[67],[11,22,68,89],[18,35],[30,42,67],
#      [17,44],[25],[21,58,68],[26,42,57,95],[],[17],[22,83],[60],
#      [26,83,84,94],[69,80,82],[41,82],[19,23,52],[20,41],[24,56],
#      [20,33],[38,71,99],[4,45],[33],[35],[47,56,64],[25,33,43,82],
#      [13,77],[14,28,66],[],[2,43],[89]]
print(Solution().isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]]))
