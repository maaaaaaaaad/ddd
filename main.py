def solution(edges, target):
  nodes = list(set([node for edge in edges for node in edge] + target))
  tree = {node: [] for node in nodes}
  answer = []

  for u, v in edges:
    tree[u].append(v)
    tree[u].sort()

  last_child = {node: 0 for node in nodes}

  for time, node in enumerate(target):
    if node == 0:
      continue

    children = tree[node]

    if last_child[node] >= len(children):
      return [-1]
    else:
      answer.append(children[last_child[node]])
      last_child[node] += 1

  return answer
