from collections import deque


def rotate(string, n):
    this = deque(string)
    this.rotate(n * -1)
    return ''.join(this)


print(rotate("This", -2))

