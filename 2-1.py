# 2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?


# this assumes ListNode is given
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# My Solution #1 (for problem 2.1)
def remove_duplicates(head: ListNode) -> ListNode:
    # TC: O(N)
    # SC: O(N)
    if not head:
        return head
    uniques = {head.val}
    current = head
    while current.next:
        if current.next.val in uniques:
            current.next = current.next.next
        else:
            uniques.add(current.next.val)
            current = current.next
    return head

# My Solution #2 (follow-up)
# follow up Qs: How would you solve this problem if a temporary buffer is not allowed?
def removeDuplicates_two(head: ListNode) -> ListNode:
    # T:O(N^2)
    # S:O(1)
    if not head:
        return head
    current = head
    while current.next:
        foo = current
        while foo.next:
            if foo.next.val == current.val:
                foo.next = foo.next.next
            else:
                foo = foo.next
        current = current.next
    return head



