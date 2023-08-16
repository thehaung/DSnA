class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    # Đề bài yêu cầu implement LRU Cache (Wiki)
    # Tiến hành lưu key của Node vào dict
    # Mỗi khi get 1 key thì sẽ xoá và add lại Node
    # Mỗi khi add thêm key, nếu key đã tồn tại thì xoá và add lại Node
    # Nếu len của dict bằng với len của LRUCache thì xoá và add lại Node
    # Ngược lại add thêm Node
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.m = dict()
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1

        p = self.m[key]
        self.deleteNode(p)
        self.addNode(p)
        self.m[key] = self.head.next
        return self.head.next.val
    # Time Complexity: O(1)
    # Space Complexity: O(1)

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            c = self.m[key]
            self.deleteNode(c)
            c.val = value
            self.addNode(c)
            self.m[key] = self.head.next
        else:
            if len(self.m) == self.size:
                prev = self.tail.prev
                self.deleteNode(prev)
                lNode = Node(key, value)
                self.addNode(lNode)
                del self.m[prev.key]
                self.m[key] = self.head.next
            else:
                lNode = Node(key, value)
                self.addNode(lNode)
                self.m[key] = self.head.next
    # Time Complexity: O(1)
    # Space Complexity: O(1)

    def addNode(self, newNode: Node) -> None:
        hNext = self.head.next
        self.head.next = newNode
        newNode.prev = self.head
        newNode.next = hNext
        hNext.prev = newNode
    # Time Complexity: O(1)
    # Space Complexity: O(1)

    def deleteNode(self, pNode: Node) -> None:
        pNode.prev.next = pNode.next
        pNode.next.prev = pNode.prev
    # Time Complexity: O(1)
    # Space Complexity: O(1)
