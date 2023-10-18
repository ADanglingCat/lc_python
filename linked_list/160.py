class Resolution:
    def test(self, headA, headB):
        lenA = 0
        lenB = 0
        curA = headA
        curB = headB
        while curA:
            lenA += 1
            curA = curA.next
        while curB:
            lenB += 1
            curB = curB.next
        if lenA > lenB:
            tempLen = lenB
            lenB = lenA
            lenA = tempLen

            curA = headB
            curB = headA

        for i in range(lenB - lenA):
            curB = curB.next

        for j in range(lenA):
            if curB == curA:
                return curB
            curA = curA.next
            curB = curB.next

        return None

