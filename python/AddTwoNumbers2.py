class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = node = ListNode(None)
        carry = 0

        while l1 or l2 :
            summ = carry

            if l1 != None:
                summ += l1.val
                l1 = l1.next

            if l2 != None:
                summ += l2.val
                l2 = l2.next
            
            # floor divide by 10 to get leftover value         
            carry = summ // 10
            node.next = ListNode(summ % 10)
            node = node.next
            print('sum: ', summ)
            print('carry: ', carry)


        if carry == 1:
            node.next = ListNode(carry)

        return dummy.next