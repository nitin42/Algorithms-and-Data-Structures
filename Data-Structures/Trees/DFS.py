def DFS(graph):
	visited, stack = set(), [root]
	while stack:
		vertex = stack.pop() # Pop the vertex
		if vertex not in visited:
			visited.add(vertex)
			stack.extend(graph[vertex] - visited)
	return visited 