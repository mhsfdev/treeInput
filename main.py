#debug!!!
from  tkinter import Tk, Canvas, mainloop
from random import randrange

canvas = Tk()
canvas = Canvas(width = 400, height = 400)
canvas.pack

class BinaryTree:

    class Node:
        def __init__(self,data, left = None, right = None):
            self.data = data
            self.left = left
            self.right = right
        def __repr__(self):
            return f'(Node data : {self.data!r}, Left child : {self.left}, Right child :{self.right})'
        
    def __init__(self, iterator = None, ord= None): 
        self.root = None
        
        
        if iterator is not None:
           for _i in iterator:
               self.add_node(_i, ord)
    
    def __len__(self):
        def len_r(_node):
            if _node == None:
                return 0
            return 1 + len_r(_node.left) + len_r(_node.right)
        
        return len_r(self.root)
    
    
    
    def add_node(self,data, ord = None): #not implemented  ord = None - random, True = left first, False = right first
        if self.root is None:
            self.root = self.Node(data)

        else :
            _node = self.root

            if ord is None:    
            
                while True:
                    if randrange(2):
                        if _node.left is None:
                            _node.left = self.Node(data)
                            return
                        _node = _node.left
                    else:
                        if _node.right is None:
                            _node.right = self.Node(data)
                            return
                        _node = _node.right
        """if ord:
                while True:
                    if _node.left is None:
                        _node.left = self.Node(data)
                        return
                    elif _node.right is None:
                        _node.right = self.Node(data)
                        return
                    else:
                        _node = _node.left    
                        """    
        




    def visualize(self):
        
        def visualize_r(node,level=0):
            _nodestr = '  '*level+'+-'     
                    
            if node.left is not None:
                visualize_r(node.left, level+len(str(node.left.data)))
            
                
            
            print (f'{_nodestr}{node.data}')    
            
            if node.right is not None:
                visualize_r(node.right,level+len(str(node.right.data)))
            else:
               
                return
        
        visualize_r(self.root,0)
          
        
        
   
    def sum_tree(self):
        def sum_tree_r(_node):
            if _node == None:
                return 0
            return _node.data + sum_tree_r(_node.left) + sum_tree_r(_node.right)

        return sum_tree_r(self.root)
    
      


def draw_Tree(node, width, x, y):
    if node is None:
        return
    canvas.create_text(x,y,text = node.data)
    canvas.pack()
    draw_Tree(node.left, width/2, x-width/2, y+40)
    draw_Tree(node.right, width/2, x+width/2, y+40)

a = BinaryTree(x for x in range(10))
a.visualize()


print('sum of tree : ',a.sum_tree())
print('lenth of tree: ',len(a))

