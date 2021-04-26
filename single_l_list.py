# A linked list is a linear data structure, 
# in which the elements are not stored at contiguous memory locations.
# The elements in a linked list are linked using pointers
class Node:
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        super().__init__()
        self.head = None

    # detect loop in the list
    def detect_loop(self, ):
        curr = self.head
        temp = set()
        while curr:
            if curr in temp:
                return True

            temp.add(curr)
            curr = curr.next
        return False

    def print_list(self):
        if self.head is None:
            print('Empty linked list')
            return

        if self.detect_loop():
            print('Loop detected in the list')
            return

        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next

    # insert new node as a head
    def push(self, new_head):
        new_node = Node(new_head)

        new_node.next = self.head

        self.head = new_node

        return new_node

    # insert the last positions
    def append(self, new_tail):
        new_node = Node(new_tail)

        if self.head == None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

        return new_node

    # insert any postion after
    def insert_after(self, prev_node, new_node):
        if prev_node.next is None:
            return self.append(new_node)

        inter_node = Node(new_node)
        inter_node.next = prev_node.next
        prev_node.next = inter_node

        return new_node

    # remove head of the linked list
    def remove_head(self):
        if self.head is None:
            print('List is empty')
            return

        self.head = self.head.next

    # remove any node by data key
    def remove_node_data(self, data):

        if self.head is None:
            print("Invalid Linked List")
            return

        temp = self.head
        prev = None
        while temp:
            if temp.data == data:
               break
            prev = temp
            temp = temp.next

        if temp is None:
            print("Invalid Node Data")
            return

        if prev is not None:
            prev.next = temp.next
        else:
            self.head = temp.next

    # remove the node by the postion key
    def delete_position(self, position):

        if self.head is None:
            print("Invalid Linked List")
            return

        iter_start = 0
        iter_node = self.head
        prev_node = None
        while iter_node:
            if position == iter_start:
                break
            prev_node = iter_node
            iter_start += 1
            iter_node = iter_node.next

        if iter_node is None:
            print("Invalid Node Position")
            return

        if prev_node is None:
            self.head = self.head.next
        else:
            prev_node.next = iter_node.next

    def delete_all_node(self):
        if self.head is None:
            print("Invalid Linked List")
            return

        curr_node = self.head
        while curr_node:
            next_node = curr_node.next

            del curr_node.data

            curr_node = next_node

        self.head = None

    # find the length of the list
    def list_length(self, ):
        if self.head is None:
            print("Invalid Linked List")
            return

        curr_node = self.head
        count = 0
        while curr_node:
            count += 1
            curr_node = curr_node.next

        return count
        # print('Total list length is :', count, ' Nodes')

    # find list length in recursively
    def len_rec(self, node=0):

        if self.head is None:
            print("Invalid Linked List")
            return 0

        if node is None:
            return 0
        else:
            return 1 + self.len_rec(node.next)

    def length(self,):
        return self.len_rec(self.head)

    # search the node exist or not
    def search(self, data_key):
        if self.head is None:
            print("Invalid Linked list")
            return

        curr_node = self.head
        while curr_node:
            if curr_node.data == data_key:
                return 'Key is found'

            curr_node = curr_node.next

        return 'Key is not found'

    # search node data in recursively
    def search_rec(self, node, key):

        if node is None:
            return 'Key is not Found'

        if node.data == key:
            return 'Key is Found'

        return self.search_rec(node.next, key)

    # get the nth node in the list

    def get_nth_node(self, position):
        if self.head is None:
            print('Invalid Linked List')
            return

        count = 0;
        curr_node = self.head
        while curr_node:
            if count == position:
                return curr_node.data

            count += 1
            curr_node = curr_node.next
        return None

    # get nth node in recursively
    def get_nth_node_rec(self, node, count, position):
        if node is None:
            return None

        if count == position:
            return node.data
        else:
            count += 1
            return self.get_nth_node_rec(node.next, count, position)

    # get the middle of list
    # my solution
    def middle_element(self, ):
        length_of_list = self.list_length()

        if not length_of_list:
            return 0

        midd_list = (length_of_list // 2)
        curr = self.head
        count = 0
        while curr:
            if count == midd_list:
                break
            count += 1
            curr = curr.next

        return curr.data

    # valid solution
    def get_middle(self, ):
        if self.head is None:
            return 0

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data

    # valid solution
    def get_middle_new(self, ):
        if self.head is None:
            return 0

        midd = self.head
        curr = self.head
        count = 0

        while curr:
            if count & 1:
                midd = midd.next
            count += 1
            curr = curr.next

        return midd.data

    # check the list is palindrome or not
    def check_palindrome(self, ):
        if self.head is None:
            return False

        front_end = self.head
        head_end = self.head
        stack = []

        while front_end:
            stack.append(front_end.data)
            front_end = front_end.next

        while head_end:
            curr = stack.pop()
            if curr is not head_end.data:
                return False

            head = head.next

        return True

    def remove_duplicates(self):
        if self.head is None:
            return False

        curr_node = self.head
        while curr_node:
            prev_node = curr_node
            initial_node = curr_node.next

            while initial_node:
               
                if curr_node.data == initial_node.data:
                    prev_node.next = initial_node.next
                    del initial_node.data
                else:
                    prev_node = initial_node

                initial_node = initial_node.next

            curr_node = curr_node.next

        return True

    def swap_nodes(self, node_one, node_two):
        if self.head is None:
            return False

        if node_one is node_two:
            return False

        curr = self.head
        prev = None
        node_one_prev = curr
        node_two_prev = curr
        while curr:
            if node_one is curr.data:
                node_one_prev = prev 
            elif node_two is curr.data:
                node_two_prev = prev 
            prev = curr
            curr = curr.next


        # if node_one_prev is None or node_two_prev is None:
        #     print('Invalid node data')
        #     return False

        # swap previous node next pointer
        if node_one_prev is None:
            temp_prev = self.head
            temp_next = node_two_prev.next
            self.head = node_two_prev.next
            self.head.next = temp_prev.next
            node_two_prev.next = temp_prev

            node_two_prev.next.next = temp_next


        else:
            temp_prev = node_one_prev.next
            node_one_prev.next = node_two_prev.next
            node_two_prev.next = temp_prev

            temp_next = node_one_prev.next.next
            node_one_prev.next.next = node_two_prev.next.next
            node_two_prev.next.next = temp_next

       

        return True
                    

    def move_last_front(self, ):
        if self.head is None:
            return False

        curr = self.head
        curr_prev = self.head

        while curr and curr.next:
            curr_prev = curr
            curr = curr.next

        curr_prev.next = None
        curr.next = self.head

        self.head = curr

        return True

        




if __name__ == '__main__':

    llist = LinkedList()
    first = Node(1)
    llist.head = first

    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    # fifth = Node(3)
    # sixth = Node(2)
    # seventh = Node(1)
    first.next = second
    
    second.next = third
    third.next = fourth
    # fourth.next = fifth
    # fifth.next = sixth
    # sixth.next = seventh

    # sixth.next = llist.head

    # add to the head of the list
    # v_first = llist.push(0)
    # for i in range(100, 200):

    #     last = llist.append(i)

    # intermediate inserts
    # llist.insert_after(v_first, 22)

    # remove head node
    # llist.remove_head()
    # llist.remove_node_data(6)
    # llist.delete_position(4)
    # llist.delete_all_node()

    # get length of the llist
    # llist.list_length()
    # recursion length
    # print(llist.length())


    # search the node
    # print(llist.search(39))
    # recursion search
    # print(llist.search_rec(node=llist.head, key=39))

    # get nth node data in the list
    # print('nth node data is: ', llist.get_nth_node(48))
    # get nth node data in the list recursively
    # print('recusive find the nth :',llist.get_nth_node_rec(node=llist.head, count=0, position=34))

    # print('midd node data is : ',llist.middle_element())
    # print('midd in pointer ', llist.get_middle())
    # print('midd in pointer two ', llist.get_middle_new())

    # print('loop detected' if llist.detect_loop() else 'no loop detected')
    # llist.remove_duplicates()


    # print('before swap')
    # llist.print_list()

    # llist.swap_nodes(1, 4)
    # print('after swap')

    llist.move_last_front()

    llist.print_list()

    

