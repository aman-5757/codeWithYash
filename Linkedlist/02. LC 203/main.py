class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        while head != None and head.val == val:
            head = head.next
            
        if head == None:
            return head
        
        temp = head
        while temp.next != None:
            if temp.next.val == val:
                temp.next  = temp.next.next
            else:
                temp = temp.next
        return head