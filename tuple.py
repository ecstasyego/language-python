x = ['a', 'c', 'b']
sorted(x, key=lambda x: x[0], reverse=False)
filter(lambda x: x[0] == 'a', x)
map(lambda x: 'Alphabet: ' + x[0], x)

x = ['a', 'c', 'b']
y = [1, 2, 3]
zip(x, y)

x = [(1, 'a'), (3, 'c'), (5, 'a'), (2, 'b'), (4, 'c'), (6, 'a'), (7, 'a'), (8, 'b')]
sorted(x, key=lambda x: x[0], reverse=False)
filter(lambda x: x[1] == 'a', x)
map(lambda x: x[0], x)
