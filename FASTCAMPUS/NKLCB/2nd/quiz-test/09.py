class Node:
    def __init__(self, d, l, r):
        self.data = d
        self.left = l
        self.right = r
    
class BST:
    def __init__(self, comp):
        self.comp = comp
        self.root = None
    
    def add(self, data):
        if self.root == None:
            self.root = Node(data, None, None)
            return
            
        else:
            self.c = self.root
            while True:
                if self.comp(self.c.data, data) < 0:
                    if self.c.left == None:
                        self.c.left = Node(data, None, None)
                        return
                    else:
                        self.c = self.c.left
                else:
                    if self.c.right == None:
                        self.c.right = Node(data, None, None)
                        return
                    else:   
                        self.c = self.c.right

    def search(self, data):
        self.c = self.root
        while self.c:
            if self.c.data == data:
                return True
            else:
                if self.comp(self.c.data, data) < 0:
                    self.c = self.c.left
                else:
                    self.c = self.c.right
        return False

bst = BST(comp = lambda a, b: hash(a) - hash(b))
for c in 'qwyhwef':
    bst.add(c)

for c in 'qwyhwefjdhfdve':
    #     11111110011001
    print(1 if bst.search(c) else 0, end ='')

# 출력
# 11111110011001