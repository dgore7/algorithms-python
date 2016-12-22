class Tree:
    def __init__(self, capacity):
        self._capacity = capacity
        self._array = [None] * capacity
        self._size = 0

    def get_left_child(self, index):
        return self._array[index*2 + 1]

    def get_right_child(self, index):
        return self._array[index*2 + 2]

    def get_parent(self, index):
        return self._array[(index-1) // 2]

    def insert(self, element):
        self._array[self._size] = element
        self._size += 1

    def __str__(self):
        nodes = 1
        level = 1
        result = []
        for i, e in enumerate(self._array):
            if e is None:
                break
            if i + 1 - nodes == 0:
                result.append(e)
                result.append('\n')
                level *= 2
                nodes += level
            else:
                result.append(e)
                result.append('\t')
        return ''.join(result)

    def __len__(self):
        return self._size


class Heap(Tree):
    def _swim(self, index):
        while index > 0:
            parent = self.get_parent(index)
            if self._array[index] < parent:
                self._array[index], self._array[(index-1) // 2] = self._array[(index-1) // 2], self._array[index]
            else:
                break
            index = (index-1) // 2

    def insert(self, element):
        super().insert(element)
        self._swim(self._size - 1)

    def del_min(self):
        if self._size < 0:
            raise IndexError('empty heap')
        self._size -= 1
        arr = self._array
        arr[0], arr[self._size] = arr[self._size], arr[0]
        to_return = arr[self._size]
        arr[self._size] = None
        self._sink(0)
        return to_return

    def _sink(self, index):
        while index*2 + 1 < self._size:
            left = self.get_left_child(index)
            right = self.get_right_child(index) if index*2 + 2 < self._size else self.get_left_child(index)
            smaller_child_index = index*2 + 1 if left < right else index*2 + 2
            if smaller_child_index < self._size and self._array[index] > self._array[smaller_child_index]:
                self._array[index], self._array[smaller_child_index] = self._array[smaller_child_index], self._array[index]
            else:
                break
            index = smaller_child_index



t = Heap(10)
t.insert("root")
t.insert("left")
t.insert("right")
t.insert("left-left")
t.insert("left-right")
t.insert("right-left")
t.insert("right-right")
print(t)
while t:
    print(t.del_min())