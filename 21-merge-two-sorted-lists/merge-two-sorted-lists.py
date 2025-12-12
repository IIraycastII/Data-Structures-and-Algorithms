# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        list_1 = []

        while list1:
            list_1.append(list1.val)
            list1 = list1.next
        
        while list2:
            list_1.append(list2.val)
            list2 = list2.next

        list_1.sort()

        # build linked list to return
        dummy = ListNode()
        curr = dummy
        for val in list_1:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next
