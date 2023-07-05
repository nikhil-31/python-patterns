"""
The max product of two elements

"""

def max_product_two_elements(arr):
    """
    Returns the maximum product of two elements
    """
    arr.sort(reverse=True)
    product = (arr[0] - 1) * (arr[1] - 0)
    return product

input_arr = [3,4,5,2]
print(max_product_two_elements(input_arr))
