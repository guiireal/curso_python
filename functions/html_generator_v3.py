def list_tag(*items):
    theList = "".join(f"<li>{item}</li>" for item in items)
    return f"<ul>{theList}</ul>"


if __name__ == "__main__":
    print(list_tag("apple", "banana", "cherry"))
