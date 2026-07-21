class MinHeap:
    """
    Min Heap for prioritizing cities by distance.
    """

    def __init__(self):
        self.heap = []

    def insert(self, city):
        self.heap.append(city)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return root

    def _heapify_up(self, index):
        parent = (index - 1) // 2

        while index > 0 and self.heap[index].distance < self.heap[parent].distance:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        size = len(self.heap)

        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left].distance < self.heap[smallest].distance:
                smallest = left

            if right < size and self.heap[right].distance < self.heap[smallest].distance:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

    def display(self):
        for city in self.heap:
            print(city)