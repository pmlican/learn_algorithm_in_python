class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 1.单链表反转
# 输入 1->2->3->4->NULL
# 输出 4->3->2->1->NULL


class Solution:
    """ 反转链表 """
    @staticmethod
    def reverse_list(head: ListNode) -> ListNode:
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev

# 循坏迭代算法需要三个临时变量：pre、head、next，临界条件是链表为None或者链表就只有一个节点。


def reverse_loop(head):
    if not head or not head.next:
        return head
    pre = None
    cur = head
    while cur:
        next = cur.next  # stash next
        cur.next = pre   # reverse
        pre = cur        # advance pre
        cur = next      # advance cur
    return pre        #  pre head at end


if __name__ == '__main__':
    h = ListNode(1)
    p1 = ListNode(2)
    p2 = ListNode(3)
    p3 = ListNode(4)

    h.next = p1
    p1.next = p2
    p2.next = p3

    # p = Solution.reverse_list(h)
    p = reverse_loop(h)
    while p:
        print(p.val)
        p = p.next
