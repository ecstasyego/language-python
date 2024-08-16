# language-python

```python
class_name = "Person"
base_classes = (object,)
attributes = {
    'get_name': lambda self: self.name,
    'set_name': lambda self, name: setattr(self, 'name', name),
}

NewClass = type(class_name, base_classes, attributes)
instance = NewClass()
instance.set_name("Alice")
instance.get_name()
```
