

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        next = head.getNext()
        if next:
            self.printLinkedListInReverse(next)
        head.printValue()