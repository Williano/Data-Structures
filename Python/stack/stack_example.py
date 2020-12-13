from stack.python_stack import Stack


def main():

    stack_container = Stack()

    print("Pushing....")
    stack_container.push(5)
    stack_container.pop()
    print("")
    stack_container.pop()
    print(stack_container.peek())


if __name__ == "__main__":
    main()
