from linked_list.ListNode import ListNode


class Resolution(object):
    def remove(self, head, n):
        dumpNode = ListNode(0, head)
        slow = dumpNode
        fast = dumpNode
        while fast:
            if n:
                n -= 1
            else:
                slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dumpNode.next