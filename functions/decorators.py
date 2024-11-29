def log(function):
    def decorator(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        result = function(*args, **kwargs)
        print(f"Result: {result}")
        return result

    return decorator


@log
def add(a, b):
    return a + b


if __name__ == "__main__":
    print(add(1, 2))
