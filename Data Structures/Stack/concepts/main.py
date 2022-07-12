import stack


def main():

    s = stack.Stack(5)

    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    #  s.push(6)
    s.printStack()

    s.pop()
    s.pop()
    s.pop()

    s.push(6)
    s.push(9)
    s.push(0)

    s.printStack()


if __name__ == "__main__":
    main()