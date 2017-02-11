import collections


class Node():
    def __init__(self, weight, left=None, right=None, value=None):
        self.weight = weight
        self.left = left
        self.right = right
        self.value = value


# das nodes
def min_node(exposed_nodes):
    smallest = exposed_nodes[0]
    index = 0
    for num in range(1, len(exposed_nodes)):
        if exposed_nodes[num].weight < smallest.weight:
            smallest = exposed_nodes[num]

    exposed_nodes.remove(smallest)

    return smallest


# das tree
def build_tree(value_list):
    exposed_nodes = []

    for char in value_list:
        exposed_nodes.append(Node(weight=value_list[char], value=char))

    while len(exposed_nodes) > 1:
        node1 = min_node(exposed_nodes)
        node2 = min_node(exposed_nodes)

        new_node = Node(weight=(node1.weight + node2.weight), left=node1, right=node2)
        exposed_nodes.append(new_node)

    return new_node


# das dict FIXME needs to actually return the dict
def build_dict(node, path, dict):
    if node is None:
        return
    if node.left is None and node.right is None:
        dict[node.value] = path
        print(dict)
        return

    build_dict(node.left, path+b'0', dict)
    build_dict(node.right, path+b'1', dict)
    return dict


def encode(infile,dict,filename):
    final_bin = b''
    for char in infile:
        final_bin += dict[char]
    print(final_bin)
    with open(filename + ".bin",'wb') as new_file:
        new_file.write(final_bin)


def decode(filename):
    with open(filename, 'rb') as read_file:
        file_bytes = read_file.read()


# Main
file = "plaintext.txt"
with open(file,"r") as plainfile:
    text = plainfile.read()
    print(text)
frequencies = collections.Counter(text)

tree = build_tree(frequencies)
char_dict = build_dict(node=tree, path=b'', dict={})
encode(text,char_dict,file)
