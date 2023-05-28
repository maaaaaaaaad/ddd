from collections import defaultdict, deque
import heapq


def solution(edges, target):

  graph = defaultdict(list)
  for u, v in edges:
    graph[u].append(v)

  child = defaultdict(list)
  for u in graph:
    child[u] = sorted(graph[u])

  curr_child = {node: 0 for node in child}

  result = []

  target_leaves = [(target[i], i + 1) for i in range(len(target))
                   if target[i] != 0]

  heapq.heapify(target_leaves)

  while target_leaves:
    num, leaf = heapq.heappop(target_leaves)
    if target[leaf - 1] == 0:
      continue

    path = []
    node = 1
    while node != leaf:
      path.append(node)

      if not child[node]:
        break
      node = child[node][curr_child[node]]

    if node != leaf:
      return [-1]

    result.append(num)
    target[leaf - 1] = 0

    for node in path:
      curr_child[node] = (curr_child[node] + 1) % len(child[node])
  return result if not any(target) else [-1]
