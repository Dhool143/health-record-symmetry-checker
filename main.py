class ListNode:
    def __init__(self, value =0, next =None):
        self.value = value
        self.next = None 
        
def isHealthRecordSymmetric(head):
        
        if head is None  or head.next is None:
            return True
        
        slow = head
        fast = head
        
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            prev = None
            current = slow
            
        while current:
                next_node = current.next
                current.next = prev
                prev = current 
                
        left = head
        right = prev
            
        while right:
                if left.value != right.value:
                    return False
                left = left.next
                right = right.next
                
            
        return True
                
                
            
            
        

    