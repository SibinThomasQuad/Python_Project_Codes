def count_nodes_in_binary_tree(n, nodes_per_level):
    if n == 0:
        return nodes_per_level
    return nodes_per_level + count_nodes_in_binary_tree(n - 1, nodes_per_level)

def print_binary_tree(n, node=1, prefix="", last=True, nodes_per_level=2):
    if n > 0:
        print(prefix, "└── " if last else "├── ", node, sep="")
        new_prefix = prefix + ("    " if last else "│   ")
        count = 1  # Count the current node
        count += print_binary_tree(n - 1, node + nodes_per_level, new_prefix, False, nodes_per_level)
        for i in range(1, nodes_per_level):
            count += print_binary_tree(n - 1, node + i, new_prefix, True, nodes_per_level)
        return count
    return 0

n = int(input("Enter the number of rounds: "))
nodes_per_level = int(input("Enter the number of nodes per level: "))
total_nodes = count_nodes_in_binary_tree(n, nodes_per_level)
print(f"Binary tree structure after {n} rounds:")
count = print_binary_tree(n, nodes_per_level=nodes_per_level)
print(f"Total nodes after {n} rounds: {total_nodes}")
