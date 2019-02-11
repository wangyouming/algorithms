graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

parents = {}

costs = {}
costs["start"] = 0

processed = []

def find_lowest_cost_node(costs):
    lowest_cost_node = None
    lowest_cost = float("inf")
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node_name = find_lowest_cost_node(costs)
while node_name:
    neighbors = graph[node_name]
    cost = costs[node_name]
    for neighbor_name in neighbors:
        new_cost = cost + neighbors[neighbor_name]
        if new_cost < costs.get(neighbor_name, float("inf")):
            costs[neighbor_name] = new_cost
            parents[neighbor_name] = node_name
    processed.append(node_name)

    node_name = find_lowest_cost_node(costs)

print(costs)