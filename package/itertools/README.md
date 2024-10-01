
```python
from itertools import count, repeat, cycle
from itertools import product, permutations, combinations
from itertools import chain, zip_longest

count(10) # infinite
repeat('Alphabet', 3) # finite
cycle(['r', 'g', 'b']) # infinite

product(['a', 'b', 'c'], ['x', 'y', 'x'], ['p', 'q', 'r', 's'])
permutations(['a', 'b', 'c'], 2)
combinations(['a', 'b', 'c'], 2)
chain(['a', 'b', 'c'], ['x', 'y'])
zip_longest(['a', 'b', 'c'], ['x', 'y'], fillvalue=None)
```
