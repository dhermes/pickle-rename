# `pickle-rename`

> An Experiment in Unpickling Moved Types

## Step 1: Save

First, we pickle a simple class that has attributes `x` and `y`:

```
$ python save_v1.py
v1: __new__(A, 11.0, 12.5)
      -> <ppkg.wickle.A object at 0x7f3939661278>
v1: __init__(<ppkg.wickle.A object at 0x7f3939661278>, 11.0, 12.5)
v1: __getnewargs__(<ppkg.wickle.A object at 0x7f3939661278>)
      -> (11.0, 12.5)
v1: __getstate__(<ppkg.wickle.A object at 0x7f3939661278>)
      -> {'x': 11.0, 'y': 12.5}
```

## Step 2: Load after changing type

We unpickle the saved `a.v1.pkl` in an environment where the
`ppkg.wickle.A` class has added an attribute `z`:

```
$ python load_v2.py
v2: __new__(A, 11.0, 12.5)
    --> <ppkg.wickle.A object at 0x7fa6fca2d5c0>
v2: __setstate__(<ppkg.wickle.A object at 0x7fa6fca2d5c0>,
                 state={'x': 11.0, 'y': 12.5})
============================================================
a = <ppkg.wickle.A object at 0x7fa6fca2d5c0>
a.__dict__ = {'x': 11.0, 'y': 12.5, 'z': 10}
```

This is handled via:

```python
def __setstate__(self, state):
    self.x = state["x"]
    self.y = state["y"]
    self.z = 10
```

## Step 3: Load after changing import path

Taking the exact same code from "Step 2", we handle the case where the
`ppkg.wickle` module moved to `p2pkg.tickle`:

```
$ python load_v3.py
v3: __new__(A, 11.0, 12.5)
      -> <p2pkg.tickle.A object at 0x7f1d5b0df128>
v3: __setstate__(<p2pkg.tickle.A object at 0x7f1d5b0df128>,
                 state={'x': 11.0, 'y': 12.5})
============================================================
a = <p2pkg.tickle.A object at 0x7f1d5b0df128>
a.__dict__ = {'x': 11.0, 'y': 12.5, 'z': 10}
```

In addition to the `__setstate__` usage, the module renaming is handled via:

```python
import pickle


class RenameUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        renamed_module = module
        if module == "ppkg":
            renamed_module = "p2pkg"
        elif module == "ppkg.wickle":
            renamed_module = "p2pkg.tickle"

        return super(RenameUnpickler, self).find_class(renamed_module, name)


def renamed_load(file_obj):
    return RenameUnpickler(file_obj).load()
```

and using `renamed_load` instead of `pickle.load`.

## References

- [Python pickling after changing a module's directory][1]
- [`find_class()`][2]

[1]: https://stackoverflow.com/q/2121874/1068170
[2]: https://docs.python.org/3/library/pickle.html#pickle.Unpickler.find_class
