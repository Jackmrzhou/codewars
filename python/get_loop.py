class Node():
	pass
node1 = Node()
node2 = Node()
node3 = Node()
node4 = Node()
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2
def loop_size(node):
	node_list = []
	while node not in node_list:
		node_list.append(node)
		node = node.next

	return len(node_list)-node_list.index(node) 
print(loop_size(node1))