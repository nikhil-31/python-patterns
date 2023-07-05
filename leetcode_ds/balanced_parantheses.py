"""
The parantheses has to be balanced.
We can use a stack to do this
"""

VAR = "[{)}]"
open_list = ["[", "{" , "("]
close_list = ["]", "}", ")"]


def balanced_stack(input_str: str):
    """
    Balanced string using a stack
    """
    stack = []
    for value in input_str:
        if value in open_list:
            stack.append(value)
        elif value in close_list:
            pos = close_list.index(value)
            if len(stack) > 0 and (open_list[pos] == stack[-1]):
                stack.pop()
            else:
                return "Unbalanced"
    return "balanced" if len(stack) == 0 else "Unbalanced"

print(balanced_stack(VAR))


def balanced_queue(driver: str):
    """
    Balanced string using a queue
    """
    open_tup = tuple('({[')
    close_tup = tuple(')}]')
    map_paran = dict(zip(open_tup, close_tup))
    queue = []
    for i in driver:
        if i in open_tup:
            queue.append(map_paran[i])
        elif i in close_tup:
            if queue and i != queue.pop():
                return "Unbalanced"
    if not queue:
        return "balanced"
    else:
        return "unbalanced"
    