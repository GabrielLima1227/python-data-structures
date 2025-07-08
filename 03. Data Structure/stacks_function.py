from stack import Stack

def is_balance(input_str):
    s = Stack()
    for c in input_str:
        if c == "(":
            s.push("")
        elif c == ")":
            popped = s.pop()
            if popped is None:
                return False
    val = s.peek()
    return val is None