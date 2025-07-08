class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, item: str) -> None:
        self.items.append(item)

    def size(self) -> int:
        return len(self.items)

    def peek(self) -> str:
        if not self.items:
            return None
        return self.items[-1]

    def pop(self) -> None:
        if not self.items:
            return None
        return self.items.pop()