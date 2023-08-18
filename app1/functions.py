def read_file():
    with open("hello.txt", 'r') as file:
        todos = file.readlines()
    return todos


def write_file(todos):
    with open("hello.txt", 'w') as file:
        file.writelines(todos)
