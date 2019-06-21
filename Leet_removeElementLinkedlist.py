class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



def removeElements(head, val):
    dummy = ListNode(-1)
    dummy.next = head
    cur = dummy
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next

    return dummy.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)

removeElements(head, 6)