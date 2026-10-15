# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for i in lists: 
            while i: 
                nodes.append(i)
                i = i.next
        nodes.sort(key=lambda n: n.val)

        res = ListNode(0)
        curr = res

        for i in nodes: 
            i.next = None 
            curr.next = i
            curr = curr.next
        curr.next = None

        return res.next