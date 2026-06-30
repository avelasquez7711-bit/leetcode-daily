'''
https://leetcode.com/problems/add-two-numbers/description/

Problem: 
    Add two numbers represented by reversed linked lists and return the sum as a new linked list.

Complexity:
    Time Complexity: O(max(m, n)) - We iterate through the lists exactly once, where m and n are the lengths of l1 and l2.
    Space Complexity: O(max(m, n)) - The length of the new linked list is at most max(m, n) + 1.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create initial node for output
        tempNode = ListNode(0)
        curr = tempNode
        carry = 0

        # loop if left digits to add or a remaining carryover
        while l1 or l2 or carry:
            # get list node values, or 0 list ended
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            # split total into new carry and node value
            carry = total // 10
            digit = total % 10  

            # append digit to result list and advance pointer
            curr.next = ListNode(digit)
            curr = curr.next

            # advance pointer of input lists if available
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return tempNode.next # skip temp head and return head of sum list
