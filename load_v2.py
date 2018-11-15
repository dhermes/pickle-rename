import pickle
import sys


def main():
    # Enable `import ppkg.wickle`
    sys.path.append("v2")

    with open("a.v1.pkl", "rb") as file_obj:
        a = pickle.load(file_obj)

    print("=" * 60)
    print("a = {}".format(a))
    print("a.__dict__ = {}".format(a.__dict__))


if __name__ == "__main__":
    main()
