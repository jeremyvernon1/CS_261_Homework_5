# Course: CS261 - Data Structures
# Assignment: 5
# Student: Jeremy Vernon
# Description: Min heap


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0
#____________________________________________________________________


    def heapify(self):
        # finds last element and that element's parent
        length = self.heap.length()
        last_pos = (length - 1)
        parent_pos = ((last_pos - 1) // 2)
        # checks if child is lower
        while parent_pos >= 0:
            # initializes variables
            left_child = 2 * parent_pos  + 1
            right_child = 2 * parent_pos + 2
            right_is_lower = False
            left_is_lower = False
            lower = 0

            # if right child exists
            if right_child < length:
                # if right child less than parent
                if self.heap[right_child] < self.heap[parent_pos]:
                    right_is_lower = True
            # if left child exists
            if left_child < length:
                # if left child less than parent
                if self.heap[left_child] < self.heap[parent_pos]:
                    left_is_lower = True

            # if both lower right and lower left children
            if right_is_lower and left_is_lower:
                # finds the lower value
                if self.heap[right_child] < self.heap[left_child]:
                    lower = right_child
                else:
                    lower = left_child
            # if lower right child, but not lower left child
            elif right_is_lower:
                lower = right_child
            # if lower left child, but not lower right child
            elif left_is_lower:
                lower = left_child

            # if at least one lower child
            if right_is_lower or left_is_lower:
                self.heap.swap(lower, parent_pos)

            # continue checking
            parent_pos -= 1

    def percolate_down(self):
        # initialize loop
        # declare variables
        parent_pos = lower = 0
        length = self.heap.length()
        # set to true to begin while loop
        right_is_lower = True
        left_is_lower = True

        # loop to percolate higher value down
        while left_is_lower or right_is_lower:
            left_child = 2 * parent_pos + 1
            right_child = 2 * parent_pos + 2
            # set to false to provide base case
            right_is_lower = False
            left_is_lower = False

            # if left child exists and is lower
            if left_child < length:
                if self.heap[left_child] < self.heap[parent_pos]:
                    left_is_lower = True

            # if right child exists and is lower
            if right_child < length:
                if self.heap[right_child] < self.heap[parent_pos]:
                    right_is_lower = True

            # if both left and right lower children
            if left_is_lower and right_is_lower:
                if self.heap[right_child] < self.heap[left_child]:
                    lower = right_child
                    left_is_lower = False
                else:
                    lower = left_child
                    right_is_lower = False

            # if only left lower child
            elif left_is_lower:
                lower = left_child
                right_is_lower = False

            # if only right child
            elif right_is_lower:
                lower = right_child
                left_is_lower = False

            # swap
            if right_is_lower or left_is_lower:
                self.heap.swap(parent_pos, lower)

            # update parent pos for next pass
            if left_is_lower:
                parent_pos = left_child
            elif right_is_lower:
                parent_pos = right_child

    def add(self, node: object) -> None:
        """
        Adds a node to the heap.
        Sorts the heap.
        """
        # add node to end
        self.heap.append((node))
        self.heapify()

    def get_min(self) -> object:
        """
        Returns the minimum value
        """
        if self.is_empty():
            raise MinHeapException
        return self.heap.data[0]

    def remove_min(self) -> object:
        """
        Removes and returns the root
        """
        if self.is_empty():
            raise MinHeapException
        min_node = self.heap[0]
        self.heap.swap(0, -1)
        self.heap.pop()
        self.percolate_down()
        return min_node

    def build_heap(self, da: DynamicArray) -> None:
        """
        Builds a heap from a given array
        """
        self.heap = DynamicArray(da.data)
        self.heapify()

#____________________________________________________________________

# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - add example 3")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in [32, 12, 2, 8, 16, 20, 24, 40, 4]:
        h.add(value)
        print(h)

    print("\nPDF - add example 4")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in [5, 2, 11, 8, 6, 20, 1, 3, 7]:
        h.add(value)
        print(h)

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())


    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
