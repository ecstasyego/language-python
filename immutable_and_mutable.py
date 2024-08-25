# immutable: int
x = 1
y = x
y += 3
print(x, y, sep=', ')

# immutable: string
x = 'abc'
y = x
y += 'def'
print(x, y, sep=', ')

# mutable: list
x = list([1,2,3])
y = x
y.append(4)
print(x, y, sep=', ')

# mutable: dict
x = dict(a=1, b=2, c=3)
y = x
y.update(d=4)
print(x, y, sep=', ')

# mutable: user defined object
A = type('A', (object, ), {'__init__':lambda self, value: setattr(self, 'value', value)})
x = A(1)
y = x
y.value = 2
print(x.value, y.value, sep=', ')
