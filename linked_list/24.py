from linked_list.ListNode import ListNode


class Solution(object):
    def swapPairs(self, head):
        res = ListNode(next=head)
        pre = res
        while pre.next and pre.next.next:
            cur = pre.next
            post = cur.next

            pre.next = post
            cur.next = post.next
            post.next = cur

            pre = pre.next.next
        return res.next