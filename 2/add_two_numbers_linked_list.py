class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        string1 = ""
        string2 = ""
        while l1 != None:
            string1 = str(l1.val) + string1
            l1 = l1.next
        while l2 != None:
            string2 = str(l2.val)+string2
            l2 = l2.next
        valor = str(int(string1) + int(string2))
        lista_enlazada = nuevo = ListNode(0)
        while valor:
            lista_enlazada.next = ListNode(int(valor[len(valor)-1]))
            valor = valor[0:len(valor)-1]
            lista_enlazada = lista_enlazada.next
        return nuevo.next
