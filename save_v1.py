"""Example output:

$ python save_v1.py
v1: __new__(A, 11.0, 12.5)
v1: __init__(<ppkg.wickle.A object at 0x7f38552eba58>, 11.0, 12.5)
v1: __getnewargs__(<ppkg.wickle.A object at 0x7f38552eba58>)
v1: __getstate__(<ppkg.wickle.A object at 0x7f38552eba58>)
"""

import pickle
import sys


def main():
    sys.path.append("v1")
    import ppkg.wickle

    a = ppkg.wickle.A(11.0, 12.5)
    with open("a.v1.pkl", "wb") as file_obj:
        pickle.dump(a, file_obj)


if __name__ == "__main__":
    main()
