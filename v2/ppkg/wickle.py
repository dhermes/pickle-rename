def _pretty_after(a, k):
    positional = ", ".join(repr(arg) for arg in a)
    keyword = ", ".join(
        "{}={!r}".format(name, value) for name, value in k.items()
    )
    if positional:
        if keyword:
            return ", {}, {}".format(positional, keyword)
        else:
            return ", {}".format(positional)
    else:
        if keyword:
            return ", {}".format(keyword)
        else:
            return ""


class A:
    def __init__(self, x, y, *, z=10):
        print("v2: __init__({}, {!r}, {!r}, z={!r})".format(self, x, y, z))
        self.x = x
        self.y = y
        self.z = z

    def __new__(cls, *args, **kwargs):
        msg = _pretty_after(args, kwargs)
        print("v2: __new__({}{})".format(cls.__name__, msg))
        return super(A, cls).__new__(cls)

    def __getnewargs__(self, *args, **kwargs):
        template = "v2: __getnewargs__({}{})"
        print(template.format(self, _pretty_after(args, kwargs)))
        raise NotImplementedError

    def __getstate__(self, *args, **kwargs):
        template = "v2: __getstate__({}{})"
        print(template.format(self, _pretty_after(args, kwargs)))
        raise NotImplementedError

    def __setstate__(self, state):
        template = "v2: __setstate__({}, state={!r})"
        print(template.format(self, state))
        self.x = state["x"]
        self.y = state["y"]
        self.z = 10
