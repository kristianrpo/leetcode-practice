# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        anterior = None
        actual = head
        while actual:
            siguiente = actual.next
            actual.next = anterior
            anterior = actual
            actual = siguiente
        return anterior