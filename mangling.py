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
print('  [M]', m.name, m._Mangling__name, sep=', ')

m.name = 'FROM OUTER'
print('  [M]', m.name, m._Mangling__name, sep=', ')

m.member1('FROM MEMBER1')
print('  [M]', m.name, m._Mangling__name, sep=', ')

m.member2('FROM MEMBER2')
print('  [M]', m.name, m._Mangling__name, sep=', ', end='\n\n')



class Inheritance(Mangling):
    def __init__(self):
        super(Inheritance, self).__init__()
        self.name = 'MANGLING'
        self.__name = 'INHERITANCE'

class ManglingOveride(Mangling):
    def __init__(self):
        super(ManglingOveride, self).__init__()
        self.name = 'MANGLING'
        self.__name = 'MANGLING OVERIDE'

    def member1(self, name):
        self.name = name

    def member2(self, name):
        self.__name = name

im = Inheritance()
iom = InheritanceOveride()
print(' [IM]', im.name, im._Mangling__name, im._Inheritance__name, sep=', ')
print('[IOM]', iom.name, iom._Mangling__name, iom._InheritanceOveride__name, sep=', ')

im.name = 'FROM OUTER'
iom.name = 'FROM OUTER'
print(' [IM]', im.name, im._Mangling__name, im._Inheritance__name, sep=', ')
print('[IOM]', iom.name, iom._Mangling__name, iom._InheritanceOveride__name, sep=', ')

im.member1('FROM MEMBER1')
iom.member1('FROM MEMBER1')
print(' [IM]', im.name, im._Mangling__name, im._Inheritance__name, sep=', ')
print('[IOM]', iom.name, iom._Mangling__name, iom._InheritanceOveride__name, sep=', ')

im.member2('FROM MEMBER2')
iom.member2('FROM MEMBER2')
print(' [IM]', im.name, im._Mangling__name, im._Inheritance__name, sep=', ')
print('[IOM]', iom.name, iom._Mangling__name, iom._InheritanceOveride__name, sep=', ')

