'''
This is my solution for the Add Two Numbers problem on Leetcode. 

Complexity:
    Time Complexity: O(max(m, n)) - We iterate through the lists exactly once, where m and n are the lengths of l1 and l2.
    Space Complexity: O(max(m, n)) - The length of the new linked list is at most max(m, n) + 1.

Problem: 
    You are given two non-empty linked lists representing two non-negative integers. 
    The digits are stored in reverse order, and each of their nodes contains a single digit. 
    Add the two numbers and return the sum as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]

Example 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]
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