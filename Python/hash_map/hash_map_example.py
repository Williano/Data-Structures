from hash_map import HashMap


def main():

    nums = HashMap()

    nums["first"] = 1
    nums["second"] = 300

    print(nums.hash_table)

    print(" ")

    print(nums["first"])

    del nums["second"]

    print(" ")

    print(nums.hash_table)


if __name__ == "__main__":
    main()
