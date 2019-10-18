import random


class ListNode:
    def __init__(self, data = None):
        self._data = data
        self._forwards = []


class SkipList:

    _MAX_LEVEL = 4

    def __init__(self):
        self._level_count = 1
        self._head = ListNode()
        self._head._forwards = [None] * self._MAX_LEVEL

    def find(self, value):
        '''
        查找一个元素，返回一个ListNode 对象
        '''
        pass

    def insert(self, value):
        '''
        插入一个结点，成功返回 True，失败返回 False
        '''
        level = self._random_level()
        if self._level_count < level: self._level_count = level
        new_node = ListNode(value)
        new_node._forwards = [None] * level
        update = [self._head] * level  # update 保存插入结节的左边的节点

        p = self._head
        for i in range(level - 1, -1, -1):
            while p._forwards[i] and p._forwards[i]._data < value:
                p = p._forwards[i]
            if p._forwards[i] and p._forwards[i]._data == value:
                # 说明已经存储该节点，不需要再插入
                return False
            update[i] = p  # 找到插入的位置

        for i in range(level):
            new_node._forwards[i] = update[i]._forwards[i]  # new_node.next = prev.next
            update[i]._forwards[i] = new_node  # prev.next = new_node
        return True



    def delete(self, value):
        pass

    def pprint(self):
        '''
        打印跳表
        '''
        skiplist_str = ''
        i = self._level_count - 1
        while i >= 0:
            p = self._head
            skiplist_str = f'head {i}: '
            while p:
                if p._data:
                    skiplist_str += '->' + str(p._data)
                p = p._forwards[i]
            print(skiplist_str)
            i -= 1

    def _random_level(self, p = 0.5):
        level = 1
        while random.random() < p and level < self._MAX_LEVEL:
            level += 1
        return level

if __name__ == "__main__":
    l = SkipList()
    for i in range(0,100,3):
        l.insert(i)
    l.pprint()