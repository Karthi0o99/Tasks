class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def create_list(linklst):

    cur = dummy = ListNode(0)
    for e in linklst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next

def numComponents(head, nums):
    s=len(nums) # 2
    while head.next:
        if head.val in nums:
            if head.next.val in nums:
                s-=1
        head=head.next
    return s

head = [0, 1, 2, 3, 4]
nums = [0, 1, 4, 3]
head = create_list(head)
print(numComponents(head, nums))