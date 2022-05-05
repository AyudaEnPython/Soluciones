"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


class Node:

    def __init__(self, data = None) -> None:
        self.data = data
        self.next = self


class CircularList:

    def __init__(self) -> None:
        self.head = None
        self.count = 0

    def __repr__(self) -> str:
        s = ""
        if self.head is None:
            return s
        s += f"{self.head.data}"
        next_ = self.head.next
        while next_ != self.head:
            s += f" -> {next_.data}"
            next_ = next_.next
        return s

    def append(self, data) -> None:
        self.insert(data, self.count)

    def insert(self, data, index) -> None:
        if index < 0 or index > self.count:
            raise IndexError("Index out of range")
        if index == 0:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.count += 1

    def remove(self, index) -> None:
        if index < 0 or index >= self.count:
            raise IndexError("Index out of range")
        if self.count == 1:
            self.head = None
            self.count = 0
        before = self.head
        for _ in range(self.count -1 if index -1 == -1 else index -1):
            before = before.next
        after = before.next.next
        before.next = after
        if index == 0:
            self.head = after
        self.count -= 1

    def remove_last(self) -> None:
        self.remove(self.count - 1)

    def index(self, data) -> int:
        if self.head is None:
            raise ValueError("List is empty")
        current = self.head
        for i in range(self.count):
            if current.data == data:
                return i
            current = current.next
        raise ValueError("Data not found")

    def size(self) -> int:
        return self.count

    def display(self) -> None:
        print(self)


if __name__ == "__main__":
    from random import shuffle, choice

    c = CircularList()
    k = choice([-1, 1])
    personas = [s for s in "abcdefghij"]
    shuffle(personas)
    for p in personas:
        c.append(p)
    c.display()
    if k > 0:
        for i in range(5, 0, -1):
            c.remove(i)
    else:
        for i in range(5):
            c.remove_last()
    c.display()
