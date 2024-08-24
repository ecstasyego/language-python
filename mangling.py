class Mangling:
    def __init__(self):
        self.name = 'MANGLING'
        self.__name = 'MANGLING'
        
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
print(m.name, m._Mangling__name, sep=', ')

m.name = 'FROM OUTER'
print(m.name, m._Mangling__name, sep=', ')

m.member1('FROM MEMBER1')
print(m.name, m._Mangling__name, sep=', ')

m.member2('FROM MEMBER2')
print(m.name, m._Mangling__name, sep=', ')



class Inheritance(Mangling):
    def __init__(self):
        super(Inheritance, self).__init__()
        self.name = 'MANGLING OVERIDE'
        self.__name = 'INHERITANCE'

    def member1(self, name):
        self.name = name

    def member2(self, name):
        self.__name = name

im = Inheritance()
print(im.name, im._Mangling__name, im._Inheritance__name, sep=', ')

im.name = 'FROM OUTER'
print(im.name, im._Mangling__name, im._Inheritance__name, sep=', ')

im.member1('FROM MEMBER1')
print(im.name, im._Mangling__name, im._Inheritance__name, sep=', ')

im.member2('FROM MEMBER2')
print(im.name, im._Mangling__name, im._Inheritance__name, sep=', ')
