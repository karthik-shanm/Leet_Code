# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def get_node_details(self, node):
        node = getattr(node,'next',None)
        node_val = getattr(node,'val',0)
        node_end = True if node == None else False
        
        return  node, node_val, node_end

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_ovr = 0
        prev_node = None
        l1_val = l1.val
        l2_val = l2.val
        l1_end = l2_end = False
        while True:
            
            sum_val = l1_val + l2_val + carry_ovr
            digit = sum_val % 10
            carry_ovr = sum_val // 10
            
            if prev_node != None:
                curr_node = ListNode(digit)
                prev_node.next = curr_node
                prev_node = curr_node
            else:
                prev_node = ListNode(digit)
                head_node = prev_node
                
            l1, l1_val, l1_end = self.get_node_details(l1)
            l2, l2_val, l2_end = self.get_node_details(l2)
            
            if l1_end==True and l2_end==True:
                if carry_ovr:
                    prev_node.next = ListNode(carry_ovr)
                break
            
        return head_node

        