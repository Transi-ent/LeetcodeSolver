class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class DoubleList:
    """
    双向链表在任意位置删除一个节点的时间复杂度为 O(1)
    """
    def __init__(self):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def addFirst(self, node: Node):
        # 先改变节点node的指针
        node.prev = self.head
        node.next = self.head.next
        # 再改变原链表上其它节点的指针
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node: Node):
        # 传过来的节点已经检查过，必然存在于双向链表上
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node

    def removeLast(self):
        if self.tail.prev == self.head:
            return None
        self.size -= 1
        return self.remove(self.tail.prev)

    def size(self):
        return self.size

class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity
        self.queue = DoubleList() # 使用一个队列记录数据的使用情况，刚使用过的放在队尾(index=len(queue)-1)

    def get(self, key: int) -> int:
        if not key in self.map.keys():
            return -1
        node = self.map.get(key)
        self.put(key, node.val)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key in self.map:# 若已经存在过，直接覆盖
            self.queue.remove(self.map[key])
            self.map[key] = node
        else:# key 还没出现过
            if len(self.map)>=self.capacity:# 检查是否超容
                last = self.queue.removeLast()
                del self.map[last.key]

            self.map[key] = node

        self.queue.addFirst(node)

def printList(head: Node):
    cur = head
    while cur:
        print(cur.val, " ->", end=' ')
        cur = cur.next

cache = LRUCache(3)
cache.put(1,1)
cache.put(2,2)
cache.get(1)
cache.put(3,3)
cache.get(2)
cache.put(4,4)
cache.get(1)
cache.get(3)
cache.get(4)
# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# dlist = DoubleList()
# dlist.addFirst(n1)
# dlist.addFirst(n2)
# dlist.addFirst(n3)
# printList(n3)
