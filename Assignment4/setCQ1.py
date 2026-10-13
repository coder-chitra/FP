class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def delete_kth(head, k):

    if head is None:
        return None

    if k == 1:
        return head.next

    head.next = delete_kth(head.next, k - 1)

    return head


def display(head):

    temp = head

    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next

    print("None")


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print("Original List:")
display(head)

head = delete_kth(head, 3)

print("After Deleting 3rd Node:")
display(head)