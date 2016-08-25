def BFS(graph):
	visited, queue = set(), [root]
	while stack:
		vertex = queue.pop(0) # Pop the vertex
		if vertex not in visited:
			visited.add(vertex)
			queue.extend(graph[vertex] - visited)
	return visited 