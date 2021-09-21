def sub_ids(node, depth, visited):
    if node.state.is_goal():
        return node
    visited.append(node)
    if depth <= 0:
        return None
    for child in node.get_children(location):
        if node_exists_in(visited, child):
            continue
        result = sub_ids(child, depth-1, visited)
        if result:
            return result
    return None
def IDS(location):
    depth = 0
    initial_state = State(*find_initial_values(location))
    initial_node = Node(initial_state)
    while True:
        visited = []
        result = sub_ids(initial_node, depth, visited)
        if depth == 13:
            print(depth)
            for v in visited:
                v.show()
            print("&&&&&&&&")
        if result:
            return result
        depth += 1
    return None

solution = IDS(location)
if solution:
    solution.show()
else:
    print("Solution does not exists!")