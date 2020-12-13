from stack.python_stack import Stack


def main():

    stack_container = Stack()

    print("Pushing....")
    stack_container.push(5)

    print("")

    print(stack_container.is_empty())


if __name__ == "__main__":
    main()
