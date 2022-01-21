from queue.python_queue import Queue


def main():

    data_queue = Queue()

    data_queue.enqueue("William")
    data_queue.enqueue("Bill")

    print(data_queue.size())


if __name__ == "__main__":
    main()
