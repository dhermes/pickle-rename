"""Example output:

$ python load_v3.py
v3: __new__(A, 11.0, 12.5)
v3: __setstate__(<p2pkg.tickle.A object at 0x7f6ed12b5080>, state={'x': 11.0, 'y': 12.5})
============================================================
<p2pkg.tickle.A object at 0x7f6ed12b5080>
{'x': 11.0, 'y': 12.5, 'z': 10}
"""

import pickle
import sys


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


def main():
    # Enable `import p2pkg.tickle`
    sys.path.append("v3")

    with open("a.v1.pkl", "rb") as file_obj:
        a = renamed_load(file_obj)

    print("=" * 60)
    print(a)
    print(a.__dict__)


if __name__ == "__main__":
    main()
