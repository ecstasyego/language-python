class Subject:
    pass

class Node:
    def __init__(self, node=None, name=None):
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
        self.tree = self
        return self
        
    @classmethod
    def posterity(cls, self):
        names = list(filter(lambda name: isinstance(getattr(self, name), cls), dir(self)))
        self.children = dict(map(lambda x: (x, getattr(self, x)), names))
        for order, (name, child) in enumerate(self.children.items()):
            child.nodename = name
        return self.children.values()

class Forest:
    class TreeManager(Node):
        subject_class = dict()
        subject = dict() 
        subject_structure = dict()
                    
        @classmethod
        def update(cls, self):
            treename = self.treename
            cls.subject_structure[treename] = self.tree
            cls.subject[treename] = self
            cls.subject_class[treename] = self.__class__
            
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
        
        subject1_component_a = self.TreeManager.subject_structure['TREE_A'].a.node
        subject1_component_b = self.TreeManager.subject_structure['TREE_A'].b.node
        subject1_component_c = self.TreeManager.subject_structure['TREE_A'].c.node
        subject1 = self.TreeManager.subject['TREE_A']
        subject2 = self.TreeManager.subject['TREE_B']
        subject1_class = self.TreeManager.subject_class['TREE_A']
        subject2_class = self.TreeManager.subject_class['TREE_B']

forest = Forest()
forest.TreeManager.subject['TREE_A']

        
