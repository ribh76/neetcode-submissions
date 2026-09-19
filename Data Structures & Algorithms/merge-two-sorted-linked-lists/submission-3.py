# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
            steps: 
            1. Create a list and output node twin 
            2. if list1.next < list2.next: 
                node = list1.next. 
                
            3. else: 
                node = list2.next
            4. 
        '''

        output = list3 = ListNode()

        while list1 and list2: 

            if list1.val < list2.val: 
                list3.next = list1
                list1 = list1.next
                list3 = list3.next
            else: 
                list3.next = list2
                list2 = list2.next
                list3 = list3.next
            
        list3.next = list1 or list2 

        return output.next

