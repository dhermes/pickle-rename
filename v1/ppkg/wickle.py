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
    def __init__(self, x, y):
        print("v1: __init__({}, {!r}, {!r})".format(self, x, y))
        self.x = x
        self.y = y

    def __new__(cls, *args, **kwargs):
        msg = _pretty_after(args, kwargs)
        print("v1: __new__({}{})".format(cls.__name__, msg))
        result = super(A, cls).__new__(cls)
        print("      -> {}".format(result))
        return result

    def __getnewargs__(self, *args, **kwargs):
        template = "v1: __getnewargs__({}{})"
        print(template.format(self, _pretty_after(args, kwargs)))
        result = self.x, self.y
        print("      -> {}".format(result))
        return result

    def __getstate__(self, *args, **kwargs):
        template = "v1: __getstate__({}{})"
        print(template.format(self, _pretty_after(args, kwargs)))
        result = {"x": self.x, "y": self.y}
        print("      -> {}".format(result))
        return result

    def __setstate__(self, state):
        template = "v1: __setstate__({}, state={!r})"
        print(template.format(self, state))
        raise NotImplementedError
