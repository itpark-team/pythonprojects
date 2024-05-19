def print_hello(current_line):
    print(f"{current_line}: hello world")
    if current_line < 10:
        print_hello(current_line + 1)

    print(f"{current_line}: recurs up")


print_hello(1)
