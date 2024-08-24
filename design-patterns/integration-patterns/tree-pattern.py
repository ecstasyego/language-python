class Subject:
    pass

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
            
        self.treename = name
        self.tree = True
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
        subject_structure = dict()
                    
        @classmethod
        def update(cls, tree):
            treename = tree.treename
            cls.subject[treename] = tree
            cls.subject_class[treename] = tree.__class__
            tree.node.TreeManager = cls
            
    def TreeComponent(self, node):
        return self.TreeManager(node)
        
    def __init__(self):
        # tree1: subject1
        tree1 = Node(Subject())
        tree1.a = Node(Subject())
        tree1.b = Node(Subject())
        tree1.c = Node(Subject())
        tree1 = Node.progeny(tree1, 'TREE_A')

        # tree2: subject2
        tree2 = Node(Subject())
        tree2.a = Node(Subject())
        tree2.b = Node(Subject())
        tree2.b.a = Node(Subject())
        tree2.b.b = Node(Subject())
        tree2.b.b.a = Node(Subject())
        tree2.c = Node(Subject())
        tree2 = Node.progeny(tree2, 'TREE_B')

        maintree = self.TreeComponent(Subject())
        maintree.a = self.TreeComponent(Subject())
        maintree.b = self.TreeComponent(Subject())
        maintree.c = self.TreeComponent(Subject())
        self.TreeManager.progeny(maintree, 'MAINTREE')
        self.TreeManager.update(tree1) 
        self.TreeManager.update(tree2) 

        # [node class]
        node1_class = self.TreeManager.subject_class['TREE_A']
        node2_class = self.TreeManager.subject_class['TREE_B']

        # [node object]: subject from TreeManager
        node1_object = self.TreeManager.subject['TREE_A']
        node2_object = self.TreeManager.subject['TREE_B']
        node3_object = self.TreeManager.subject['TREE_B'].a
        subject1 = self.TreeManager.subject['TREE_A'].node
        subject2 = self.TreeManager.subject['TREE_B'].node
        subject1.TreeManager # root node TreeManager
        subject2.TreeManager # root node TreeManager
        
        # [TreeManager] from node object: subject
        tree1.a.mediate(self.TreeManager)
        tree1.b.mediate(self.TreeManager)
        tree1.a.node.TreeManager
        tree1.b.node.TreeManager

forest = Forest()
forest.TreeManager.subject['TREE_A']
forest.TreeManager.subject_class['TREE_A']
