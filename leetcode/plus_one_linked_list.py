class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        carry = self.calcCarry(head)
        if carry > 0:
            head = ListNode(carry, head)
        print(head)
        return head

    def calcCarry(self, node):
        if node.next is None:
            carry = 1
        else:
            carry = self.calcCarry(node.next)
        v = node.val + carry
        node.val = v % 10
        return v // 10

l = ListNode(1, ListNode(2, ListNode(3)))
s = Solution()
s.plusOne(l)