from collections import defaultdict


def dfs(node, parent, graph, values, sums):
  sums[node] = values[node - 1]
  for child in graph[node]:
    if child == parent:
      continue
    dfs(child, node, graph, values, sums)
    sums[node] += sums[child]


def solution(values, edges, queries):
  n = len(values)
  graph = defaultdict(list)
  for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)
  sums = [0] * (n + 1)
  dfs(1, 0, graph, values, sums)
  answer = []
  for u, w in queries:
    if w == -1:
      answer.append(sums[u])
    else:
      diff = w - values[u - 1]
      values[u - 1] = w
      while u != 1:
        sums[u] += diff
        u = graph[u][0] if graph[u][0] != parent else graph[u][1]
      sums[1] += diff
  return answer
