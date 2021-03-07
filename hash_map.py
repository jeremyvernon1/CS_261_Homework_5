# Course: CS261 - Data Structures
# Assignment: 5
# Student: Jeremy Vernon
# Description: hash maps


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        """
        Clears the contents of the hash table
        """
        if self.size > 0:
            for index in range(self.capacity):
                curr_length = self.buckets[index].length()
                if curr_length > 0:
                    self.buckets[index] = LinkedList()
                    self.size -= curr_length

    def get(self, key: str) -> object:
        """
        Returns the value of the associated key.
        Returns None if not found.
        """
        if self.size > 0:
            hash = hash_function_1(key)
            index = hash % self.capacity
            destination = self.buckets[index]
            for node in destination:
                if node.key == key:
                    return node.value
                if node.next is None:
                    return None
        return None

    def put(self, key: str, value: object) -> None:
        """
        Adds a new value to the hash table
        """
        # initializes
        hash = hash_function_1(key)
        # print("hash:", hash)
        array_size = self.size
        index = hash % self.capacity
        ## insert_at2 = hash_function_2(key)
        # print("index:", index, "; capacity:", self.capacity, "; size:", self.size, "; key:", key, "; value:", value)
        destination = self.buckets[index]
        # resolves collision
        if array_size > 0:
            if destination.length() > 0:
                for node in destination:
                    if node.key == key:
                        node.value = value
                        return
                    if node.next is None:
                        break
        # inserts new key value pair
        destination.insert(key, value)
        self.size += 1

    def remove(self, key: str) -> None:
        """
        Removes the node that matches the given key
        """
        if self.size > 0:
            hash = hash_function_1(key)
            index = hash % self.capacity
            destination = self.buckets[index]
            # if more than one item in SLL
            if destination.length() > 1:
                for node in destination:
                    if node.next is not None and node.next.key == key:
                        node.next = node.next.next
                        self.size -= 1
            # if one item in SLL
            else:
                for node in destination:
                    if node.key == key:
                        self.buckets[index] = LinkedList()
                        self.size -= 1

    def contains_key(self, key: str) -> bool:
        """
        Searches for a key. Returns True if found and False if not.
        """
        if self.size > 0:
            hash = hash_function_1(key)
            index = hash % self.capacity
            destination = self.buckets[index]
            for node in destination:
                if node.key == key:
                    return True
                if node.next is None:
                    return False
        return False

    def empty_buckets(self) -> int:
        """
        Counts the number of empty buckets
        """
        count = 0
        for index in range(self.capacity):
            if self.buckets[index].length() == 0:
                count += 1
        return count

    def table_load(self) -> float:
        """
        Returns the percentage of the table that is filled
        """
        return self.size / self.capacity

    def resize_table(self, new_capacity: int) -> None:
        """
        TODO: if smaller capacity; rehash links
        """
        if new_capacity > 1:
            # if increasing
            if new_capacity > self.capacity:
                new_buckets = new_capacity - self.capacity
                while new_buckets > 0:
                    self.buckets.append(LinkedList())
                    new_buckets -= 1
            # if decreasing
            else:
                remove_buckets = self.capacity - new_capacity
                while remove_buckets > 0:
                    for old_node in self.buckets[(new_capacity + remove_buckets - 1)]:
                        # rehash
                        hash = hash_function_1(old_node.key)
                        array_size = self.size
                        index = hash % new_capacity
                        destination = self.buckets[index]
                        if array_size > 0:
                            if destination.length() > 0:
                                for node in destination:
                                    if node.key == old_node.key:
                                        node.value = old_node.value
                                        break
                                    if node.next is None:
                                        break
                        # inserts new key value pair
                        destination.insert(key, old_node.value)
                        remove_buckets -= 1

            self.capacity = new_capacity

    def get_keys(self) -> DynamicArray:
        """
        Gets all of the keys in a hash table
        """
        result_array = DynamicArray()
        for index in range(self.capacity):
            if self.buckets[index].length() > 0:
                for node in self.buckets[index]:
                    if node.key is not None:
                        result_array.append(node.key)
                    if node.next is None:
                        break
        return result_array


# BASIC TESTING
if __name__ == "__main__":

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(100, hash_function_1)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 10)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key2', 20)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 30)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key4', 40)
    print(m.empty_buckets(), m.size, m.capacity)


    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.size, m.capacity)


    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(100, hash_function_1)
    print(m.table_load())
    m.put('key1', 10)
    print(m.table_load())
    m.put('key2', 20)
    print(m.table_load())
    m.put('key1', 30)
    print(m.table_load())


    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(m.table_load(), m.size, m.capacity)

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(100, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)


    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(50, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    print(m.size, m.capacity)
    m.put('key2', 20)
    print(m.size, m.capacity)
    m.resize_table(100)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)


    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(40, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(10, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))


    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)


    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(30, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))


    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(150, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.size, m.capacity)
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)


    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(50, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')


    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))


    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            result &= m.contains_key(str(key))
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))


    print("\nPDF - get_keys example 1")
    print("------------------------")
    m = HashMap(10, hash_function_2)
    for i in range(100, 200, 10):
        m.put(str(i), str(i * 10))
    print(m.get_keys())

    m.resize_table(1)
    print(m.get_keys())

    m.put('200', '2000')
    m.remove('100')
    m.resize_table(2)
    print(m.get_keys())
