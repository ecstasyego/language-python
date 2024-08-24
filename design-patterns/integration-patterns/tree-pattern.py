class Topic:
    pass
    
class Subject_A:
    def __init__(self):
        tree = Node(Topic())
        tree.a = Node(Topic())
        tree.b = Node(Topic())
        tree.c = Node(Topic())
        self.tree = Node.progeny(tree, 'TREE_A')

class Subject_B:
    def __init__(self):
        tree = Node(Topic())
        tree.a = Node(Topic())
        tree.b = Node(Topic())
        tree.b.a = Node(Topic())
        tree.b.b = Node(Topic())
        tree.b.b.a = Node(Topic())
        tree.c = Node(Topic())
        self.tree = Node.progeny(tree, 'TREE_B')

class Node:
    def __init__(self, node=None, name=None):
        self.tree = False
        self.node = node
        self.nodename = name

    @classmethod
    def progeny(cls, self, name):
        children = cls.posterity(self)
        while children:
            _children = list()
            for child in children:
                _children.extend(cls.posterity(child))
            children = _children
            
        self.tree = True
        self.treename = name
        return self
        
    @classmethod
    def posterity(cls, self):
        names = list(filter(lambda name: isinstance(getattr(self, name), cls), dir(self)))
        self.children = dict(map(lambda x: (x, getattr(self, x)), names))
        for order, (name, child) in enumerate(self.children.items()):
            child.nodename = name
        return self.children.values()

    def mediate(self, TreeManager):
        self.node.TreeManager = TreeManager
        
class Forest:
    class TreeManager(Node):
        subject_class = dict()
        subject = dict() 
        forest = dict()
                    
        @classmethod
        def update(cls, subject):
            treename = subject.tree.treename
            cls.forest[treename] = subject.tree
            cls.subject[treename] = subject
            cls.subject_class[treename] = subject.__class__
            subject.tree.node.TreeManager = cls
            
    def TreeComponent(self, node):
        return self.TreeManager(node)
        
    def __init__(self):
        tree = self.TreeComponent(Topic())
        tree.a = self.TreeComponent(Topic())
        tree.b = self.TreeComponent(Topic())
        tree.c = self.TreeComponent(Topic())
        self.tree = self.TreeManager.progeny(tree, 'MAINTREE')
        self.TreeManager.update(Subject_A()) 
        self.TreeManager.update(Subject_B()) 

        # [node class]
        node1_class = self.TreeManager.subject_class['TREE_A']
        node2_class = self.TreeManager.subject_class['TREE_B']

        # [node object]: subject from TreeManager
        tree_A = self.TreeManager.forest['TREE_A'] # rootnode object
        tree_B = self.TreeManager.forest['TREE_B'] # rootnode object
        tree_Ba = self.TreeManager.forest['TREE_B'].a # node object
        tree_A = self.TreeManager.subject['TREE_A'].tree 
        tree_B = self.TreeManager.subject['TREE_B'].tree
        tree_Ba = self.TreeManager.subject['TREE_B'].tree.a

        # [TreeManager] from rootnode subject
        subject1 = self.TreeManager.subject['TREE_A'].tree.node # rootnode subject: topic object
        subject2 = self.TreeManager.subject['TREE_B'].tree.node # rootnode subject: topic object
        subject1.TreeManager # rootnode subject TreeManager
        subject2.TreeManager # rootnode subject TreeManager
        
        # [TreeManager] from node subject
        tree_A.a.mediate(self.TreeManager)
        tree_A.b.mediate(self.TreeManager)
        tree_A.a.node.TreeManager
        tree_A.b.node.TreeManager

forest = Forest()
forest.TreeManager.subject['TREE_A']
forest.TreeManager.subject_class['TREE_A']
