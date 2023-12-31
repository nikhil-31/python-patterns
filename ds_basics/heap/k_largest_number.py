
import heapq


class KthLargest:


    def __init__(self, k, nums):
        self.top_k_heap = []
        self.k = k

        for num in nums:
            self.add(num)


    def add(self, val):
        pass

