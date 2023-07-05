import pdb

def max(lst):
    max_num = -float('inf')
    for num in lst:
        if num > max_num:
            pdb.set_trace()
            max_num = num
    return max_num


lst = max([-1, -2, -3])