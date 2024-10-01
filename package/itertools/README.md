
```python
from itertools import count, repeat, cycle
from itertools import product, permutations, combinations
from itertools import chain, zip_longest, starmap
from itertools import islice, filterfalse, takewhile, dropwhile

count(10) # infinite
repeat('Alphabet', 3) # finite
cycle(['r', 'g', 'b']) # infinite

product(['a', 'b', 'c'], ['x', 'y', 'x'], ['p', 'q', 'r', 's'])
permutations(['a', 'b', 'c'], 2)
combinations(['a', 'b', 'c'], 2)

chain(['a', 'b', 'c'], ['x', 'y'])
zip(['a', 'b', 'c'], ['x', 'y', 'z'])
zip_longest(['a', 'b', 'c'], ['x', 'y'], fillvalue=None)
map(lambda x: (x[0], x[1]), [('a', 'x'), ('b', 'y'), ('c', 'z')])
starmap(lambda x: (x[0], x[1]), [('a', 'x'), ('b', 'y'), ('c', 'z')])

islice(['a', 'b', 'c', 'd', 'e'], 2, 5)
filter(lambda x: x == 'a', ['a', 'b', 'c'])
filterfalse(lambda x: x == 'a', ['a', 'b', 'c'])
takewhile(lambda x: x == 'a', ['a', 'b', 'c'])
dropwhile(lambda x: x == 'a', ['a', 'b', 'c'])
```
