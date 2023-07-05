# Sorting algorithms 


### sorting algorithms keywords

- Runtime - How quickly the sorting algorithm runs (O(n), O(n log(n), O(n^2), etc ...))
- Stable sort - A sorting algorithm that generates stable results when sorted multiple times
  (eg - A list sorted alphabetically, then by price, are the items that are equal sorted 
  alphabetically?)
- In-place sort - A sorting algorithm that **does not** require any additional memory space 
  other than the memory taken up by its input.
- Out of place sort - A sorting algorithm that requires additional memory space 
  other than the memory taken up by its input.
- Pathological case - A case in which input data is specifically designed to make your 
  algorithm run as slowly as possible. 


### Why does sorting matter

- Searching - Searching an item is much faster if the list is sorted
- Selection - Selecting items from a list based on their relationship to the rest of the items
is easier with sorted data. For example, finding the kth largest or smallest value, or finding
the median value of the list, is much easier when the values are in ascending or descending order
- Duplicates - Finding duplicate values in a list can be done very quickly when the list is sorted
- Distribution - Analyzing frequency distribution items on list is very fast if the list is sorted.
For example, finding the element that appears most of least often is relatively straightforward 
with a sorted list.