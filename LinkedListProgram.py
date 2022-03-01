class Node:
    def __init__(self):
        self.info = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.start = None

    # Creation of Linked list
    def create(self):
        self.start = None
        while True:
            node = Node()
            try:
                node.info = int(input("Enter value:"))
            except:
                break
            if self.start is None:
                self.start = node
            else:
                temp.next = node
            temp = node
            # ch = input("Do you want more terms? y or n")
            # if ch == "n":
            # break

    # Displaying Linked List
    def display(self):
        temp = self.start
        while temp.next is not None:
            print(temp.info, end="->")
            temp = temp.next
        print(temp.info)

    # Insertion at beginning
    def insert_at_beg(self):
        value = int(input("Enter value to be inserted:"))
        if self.start is None:
            print("No lInked list found")
            return
        node = Node()
        node.info = value
        node.next = self.start
        self.start = node

    # Insertion at last
    def insert_at_last(self):
        value = int(input("Enter value to be inserted:"))
        temp = self.start
        if self.start is None:
            print('No Linked List found')
            return
        while temp.next is not None:
            temp = temp.next
        node = Node()
        node.info = value
        temp.next = node

    # Insert after a given node
    def insert_after_given_node(self):
        value = int(input("Enter value after which node is to be inserted:"))
        temp = self.start
        if temp is None:
            print("No Linked List found")
            return
        while temp.next is not None and temp.info != value:
            temp = temp.next
        if temp is None:
            print("Value does not found")
            return
        node = Node()
        node.info = int(input("Enter info:"))
        node.next = temp.next
        temp.next = node

    # Deletion from beginning
    def delete_from_beg(self):
        if self.start is None:
            print("No Linked List found")
            return
        self.start = self.start.next

    # Deletion from end
    def delete_from_end(self):
        if self.start is None:
            print("No Linked List found")
            return
        temp = self.start
        if temp.next is None:
            temp = None
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    # Delete a given node
    def delete_given_node(self):
        value = int(input("Enter value after which node is to be deleted:"))
        temp = self.start
        if self.start is None:
            print("No LL found")
            return
        while temp.next.next is not None and temp.next.info != value:
            temp = temp.next
        if temp is None:
            print("Value not found")
            return
        temp.next = temp.next.next

    # Searching in Linked List
    def search(self):
        value = int(input("Enter value to search:"))
        temp = self.start
        if self.start is None:
            print("No linked list found")
            return
        while temp is not None and temp.info != value:
            temp = temp.next
        if temp is None:
            print("Value not found")
            return
        else:
            print("Value found")
            print(temp)

    # Reversal of Linked List
    def reversal(self):
        curr = self.start
        prev = None
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.start = prev

    # Merging of two linked list
    def mergeLL(self, l2):
        temp = self.start
        while temp.next is not None:
            temp = temp.next
        temp.next = l2.start

    # Sorting in list
    def sorting(self):
        i = self.start
        while i.next is not None:
            j = i.next
            while j is not None:
                if j.info < i.info:
                    temp = i.info
                    i.info = j.info
                    j.info = temp
                j = j.next
            i = i.next


obj = LinkedList()
func_dict = {1: obj.create,
             2: obj.display,
             3: obj.insert_at_beg,
             4: obj.insert_at_last,
             5: obj.insert_after_given_node,
             6: obj.delete_from_beg,
             7: obj.delete_from_end,
             8: obj.delete_given_node,
             9: obj.search,
             10: obj.reversal,
             11: obj.mergeLL,
             12: obj.sorting}
while True:
    print("""
    1.To create
    2.To display
    3.To insert at beginning
    4.To insert at last
    5.To insert after given node
    6.Delete from beginning
    7.Delete from last
    8.Delete after given node
    9.To search an element
    10.To reverse Linked List
    11.Merging of two linked list
    12.Sorting in Linked list
    13.Exit
    """)
    ch = int(input())
    if ch == 13:
        break
    func_dict[ch]()
