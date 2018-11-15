"""Example output:

$ python load_v2.py
v2: __new__(A, 11.0, 12.5)
v2: __setstate__(<ppkg.wickle.A object at 0x7fbd9391d198>, state={'x': 11.0, 'y': 12.5})
============================================================
<ppkg.wickle.A object at 0x7fbd9391d198>
{'x': 11.0, 'y': 12.5, 'z': 10}
"""

import pickle
import sys


def main():
    # Enable `import ppkg.wickle`
    sys.path.append("v2")

    with open("a.v1.pkl", "rb") as file_obj:
        a = pickle.load(file_obj)

    print("=" * 60)
    print(a)
    print(a.__dict__)


if __name__ == "__main__":
    main()
