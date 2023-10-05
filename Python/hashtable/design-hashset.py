from collections import defaultdict


class MyHashSet:

    def __init__(self):
        self.map = defaultdict(bool)

    def add(self, key: int) -> None:
        self.map[key] = True

    def remove(self, key: int) -> None:
        self.map[key] = False

    def contains(self, key: int) -> bool:
        return self.map[key]
