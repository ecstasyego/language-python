class Mangling:
    def __init__(self):
        self.name = 'INIT'
        
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def member1(self, name):
        self.name = name

    def member2(self, name):
        self.__name = name

m = Mangling()
print(m.name, m._Mangling__name)

m.name = 'FROM OUTER'
print(m.name, m._Mangling__name)

m.member1('FROM MEMBER1')
print(m.name, m._Mangling__name)

m.member2('FROM MEMBER2')
print(m.name, m._Mangling__name)



class Inheritance(Mangling):
    def __init__(self):
        super(Inheritance, self).__init__()
        self.name = 'INIT'

im = Inheritance()
print(im.name, im._Mangling__name)

im.name = 'FROM OUTER'
print(im.name, im._Mangling__name)

im.member1('FROM MEMBER1')
print(im.name, im._Mangling__name)

im.member2('FROM MEMBER2')
print(im.name, im._Mangling__name)
