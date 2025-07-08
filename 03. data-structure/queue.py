class Queue:
    def __init__(self) -> None:
        self.items = []

    def push(self, item: str) -> None:
        self.items.insert(0,item) 

    def pop(self) -> None:
        if not self.items:
            return None
        return self.items.pop()

    def peek(self) -> None:
        if not self.items:
            return None
        return self.items[-1]

    def size(self) -> int:
        len(self.items)