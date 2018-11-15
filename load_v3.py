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
    print("a = {}".format(a))
    print("a.__dict__ = {}".format(a.__dict__))


if __name__ == "__main__":
    main()
