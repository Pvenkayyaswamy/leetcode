# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        
        while current and current.next:
            left = current
            right = current.next
            
            gcd_val = math.gcd(left.val, right.val)
            
            temp = ListNode(gcd_val)
            left.next = temp
            temp.next = right
            
            current = right
        
        return head