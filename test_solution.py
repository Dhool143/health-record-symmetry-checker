
import unittest 
from main import (ListNode, isHealthRecordSymmetric)




def build_list(values):
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
        
        return dummy.next
        
        
        

class TestHealthRecord( unittest.TestCase):
    
    # Normal case
    
    
    def test_palindrome_odd(self):
        head = build_list([80, 90, 100, 90,80])
        
        self.assertTrue(isHealthRecordSymmetric)
        
        
    def test_palindrome_even(self):
        head = build_list([70, 85, 85, 70])
        
        self.assertTrue(isHealthRecordSymmetric)
        
        
    def test_no_palindrome(self):
        
        head = build_list([60, 70, 80])
        
        self.assertTrue(isHealthRecordSymmetric)
        
        
        
        
        #Edge case
        
        
    def test_single_node(self):
        
        head = build_list([100])
        
        self.assertTrue(isHealthRecordSymmetric)
        
        
    def test_two_different_node(self):
        head = build_list([90, 100])
        
        self.assertTrue(isHealthRecordSymmetric)
        
        
    def test_empty_list(self):
        self.assertTrue(isHealthRecordSymmetric(None))
        
        
        
if __name__ == "__main__":
        unittest.main()
        