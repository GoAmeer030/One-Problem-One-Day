class Solution:
    def delete_node(self, head, x):
        if x ==1 :
            head =head.next
            head.prev=None
            return head
        x = x -1
        nextNode = head
        while x > 0:
            nextNode = nextNode.next 
            x = x-1
        if nextNode.next:
            nextNode.next.prev = nextNode.prev
        nextNode.prev.next = nextNode.next
        del nextNode
        
        return head
