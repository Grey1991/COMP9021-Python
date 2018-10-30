from binary_tree import *

t = BinaryTree(1); t_L = BinaryTree(2); t_LL = BinaryTree(4);t_LR = BinaryTree(5)
t_R = BinaryTree(3); t_RL = BinaryTree(6)
t.left_node = t_L; t_L.left_node = t_LL ; t_L.right_node = t_LR
t.right_node = t_R; t_R.left_node = t_RL

# t.print_binary_tree()
L = [t]
for i in L:
    if i.left_node:
        L.append(i.left_node)
    if i.right_node:
        L.append(i.right_node)

L_value = [i.value for i in L if i.value]
print(L_value)
L_value = L_value[::-1]

new_tree = [t]
for i in new_tree:
    if L_value:
        i.value = L_value[0]
        i.left_node = BinaryTree()
        i.right_node = BinaryTree()
        new_tree.append(i.left_node)
        new_tree.append(i.right_node)
        L_value.pop(0)
t.print_binary_tree()


