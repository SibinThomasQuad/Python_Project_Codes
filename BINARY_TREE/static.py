def count_nodes_in_binary_tree(n):
    if n == 0:
        return 1
    return 2 ** n + count_nodes_in_binary_tree(n - 1)

def print_binary_tree(n, node=1, prefix="", last=True):
    if n > 0:
        print(prefix, "└── " if last else "├── ", node, sep="")
        new_prefix = prefix + ("    " if last else "│   ")
        count = 1  # Count the current node
        count += print_binary_tree(n - 1, node * 2, new_prefix, False)
        count += print_binary_tree(n - 1, node * 2 + 1, new_prefix, True)
        return count
    return 0

n = int(input("Enter the number of rounds: "))
total_nodes = count_nodes_in_binary_tree(n)
print(f"Binary tree structure after {n} rounds:")
count = print_binary_tree(n)
print(f"Total nodes after {n} rounds: {total_nodes}")
