from stack.python_stack import Stack


def reverse_string(sentence):

    stack_container = Stack()

    splitted_sentence = sentence.split(" ")

    for word in splitted_sentence:
        stack_container.push(word[::-1])

    for word in range(len(splitted_sentence)):
        print(stack_container.pop())


def main():

    sentence = "We will conquere COVID-19"

    reverse_string(sentence)


if __name__ == "__main__":
    main()
