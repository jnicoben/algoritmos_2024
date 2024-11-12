
class BinaryTree:

    class __Node:
        def __init__(self, value, left=None, right=None): #Left y Right estan vacios, si no reciben los toma como None.
            self.value = value
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def insert_node(self, value):
        def __insert(root, value):
            if root is None:
                print('crear nodo')
                return BinaryTree.__Node(value)
            elif value < root.value: #Inserta Izquierda
                print('insertar derecha')
                root.left = __insert(root.left, value)
            else: #Inserta derecha
                print('insertar izquierda')
                root.right = __insert(root.right, value)
            return root
        self.root = __insert(self.root, value)

        def preorden(self):
            def __preorden():

        

tree = BinaryTree()
tree.insert_node(19)
tree.insert_node(7)
tree.insert_node(31)
tree.insert_node(11)

print(tree.root.value, tree.root.left.value, tree.root.right.value, tree.root.left.right.value)






