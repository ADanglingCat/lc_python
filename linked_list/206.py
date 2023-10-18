class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # pre = None
        # cur = head
        # while cur is not None:
        #     temp = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = temp
        # return pre
        def reverse(pre, cur):
            if not cur:
                return pre
            temp = cur.next
            cur.next = pre
            return reverse(cur, temp)
        return reverse(None, head)


solution = Solution()
head = ListNode(0, ListNode(1, ListNode(2)))

head = solution.reverseList(head)
while head is not None:
    print(head.val)
    head = head.next

