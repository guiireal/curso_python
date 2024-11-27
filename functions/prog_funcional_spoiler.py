def execute(fn):
    if callable(fn):
        fn()


def welcome():
    print("Welcome to Python!")


def goodbye():
    print("Goodbye!")


if __name__ == "__main__":
    execute(welcome)
    execute(goodbye)
