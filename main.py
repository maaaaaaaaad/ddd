def solution(edges, target):
  from collections import defaultdict
  nodes = defaultdict(list)
  for u, v in edges:
    nodes[u].append(v)
  nodes = dict(nodes)

  visit_order = {key: 0 for key in nodes.keys()}

  answer = []

  for node in target:
    if node == 0:
      continue
    if node not in nodes or visit_order[node] >= len(nodes[node]):
      return [-1]
    else:
      answer.append(nodes[node][visit_order[node]])
      visit_order[node] += 1

  return answer
