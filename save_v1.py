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
