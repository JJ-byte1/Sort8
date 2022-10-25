#This is a ordered binary search treee. The tree will be ordered relative to the first location on the map.
#1. The next two locations that are closest to the first location will be input as children into the tree.
#   Ordered from min to max.
#2. Then the next two locations closest to one of the child nodes is input as children of that child node.
#3. Nodes that have already been added will be blacklisted.

class binaryTree:

    class Node:
        def __init__(self, k, v, parent = None):
            self.left = None
            self.right = None
            self.parent = parent
            self.key = k
            self.value = v


    def __init__(self, k, v):
        self._root = self.Node(k,v)
        self._currentNode = self._root

    '''
    Finds the distance from the child and the parent node.
        
        parameters:
            child(string): 'l' indicates distance between left child and parent
                           'r' distance between right child and parent
        returns:
            (float): distance in km
    '''
    def child_dist(self, child):
        node = self._currentNode
        if child == 'l':
            child_node = node.left
        elif child == 'r':
            child_node = node.right
        return ((child_node.value[0]-node.value[0])**2 + (child_node.value[1]-node.value[1])**2)**0.5 #equation to find distance



    def insert(self, k, v):
        node = self._currentNode
        distance = ((v[0]-node.value[0])**2 + (v[1]-node.value[1])**2)**0.5

        #Check if any child is empty, if so insert new node
        if self._currentNode.left == None and self._currentNode.right == None:
            self._currentNode.left = self.Node(k,v, self._currentNode)

        # elif self._currentNode.right == None:
        #     self._currentNode.right = self.Node(k, v)

        else:
            # Breadth first search to node where inserted value has shorter distance to it than one of its children.
            #Code needs to be implemented


            if distance < self.child_dist('l'):
                start = self._currentNode

                # traverse to bottom from node found in above code. Pathway is to the right child each time
                # e.g. node found through bfs -> right child -> right child -> right child -> ... -> bottom node
                while self._currentNode.right!= None:
                    self._currentNode = self._currentNode.right
                print(self._currentNode.value)

                # rearrange nodes
                ''' Rearrengement method : bottom node to left child pos, left sibling of bottom node to bottom nodes prior position,
                    bottom node parent to left siblings prior position.
                    Rearrangement continues upward until it reaches the original node found in the bfs.
                '''
                while self._currentNode.right != start:
                    self._currentNode.left = self._currentNode
                    self._currentNode.parent.left = self._currentNode
                    self._currentNode = self._currentNode.parent

                self._currentNode.left = self.Node(k,v, self._currentNode)

            self._currentNode = self._root

    def showtree(self):
        print(self._currentNode.left.value)


treee = binaryTree(10, [80,20])
treee.insert(50,[40,30])
treee.insert(20,[80,19])
treee.insert(20,[])

treee.showtree()













