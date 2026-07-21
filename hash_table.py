class HashTable:
    """
    Hash Table for storing City objects.
    """

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, city_name):
        return sum(ord(char) for char in city_name) % self.size

    def insert(self, city):
        index = self._hash(city.name)

        for stored_city in self.table[index]:
            if stored_city.name == city.name:
                return

        self.table[index].append(city)

    def search(self, city_name):
        index = self._hash(city_name)

        for city in self.table[index]:
            if city.name == city_name:
                return city

        return None

    def delete(self, city_name):
        index = self._hash(city_name)

        for i, city in enumerate(self.table[index]):
            if city.name == city_name:
                del self.table[index][i]
                return True

        return False

    def display(self):
        for bucket in self.table:
            for city in bucket:
                print(city)