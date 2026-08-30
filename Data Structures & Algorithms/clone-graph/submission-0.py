class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = {}
        q = deque([node])
        visited[node] = Node(node.val)
        while q:
            n = q.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])
        return visited[node]