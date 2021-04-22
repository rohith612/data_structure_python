class Node:
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        super().__init__()
        self.head = None
    
    # set the head of the list -> initial task
    def make_head(self, node):
        if self.head is not None:
            print('CList already has Head Node')
        else:  
            self.head = node
            node.next = node
        return

    # print all the node data in the list
    def traverse_list(self):
        current = self.head
        head = self.head
        while True:
            print(current.data)
            if current.next == head:
                break
            
            current = current.next
        
        return

    # find the length of the list
    def list_length(self):
        curr = self.head
        counter = 1
        while True:
            if curr.next is self.head:
                break
            counter += 1
            curr = curr.next

        return counter
    
    #  find the length of the list with recursive method
    def list_len_rec(self, node):
        if self.head is None:
            return 0
        
        if node.next is self.head:
            return 1
        else:
            return 1 + self.list_len_rec(node.next)


    # add tail nodes in the list for seperate function
    def append_node(self, node):
        if self.head is None:
            self.make_head(node)
            return
        
        curr = self.head
        head = self.head

        if curr.next is None:
            curr.next = node
            node.next = head
            return

        while True:
            if curr.next == head:
                break
            curr = curr.next
        
        curr.next = node
        node.next = head
        return

    # add new node as head in seperate function
    def push_head(self, node):
        head = self.head
        if head is None:
            self.make_head(node)
            return

        curr = head

        while True:
            if curr.next == head:
                break
            curr = curr.next

        tail = curr
        tail.next = node

        node.next = head
        self.head = node

        return node.data

    # find the nth node data by given position ==> [0...N]
    def get_nth_node(self, position):
        head = self.head
        if head is None:
            return None
            
        curr = head
        counter = 0
      
        while True:
            if curr.next is head:
                if counter < position:
                    curr = None
                    break

            if counter == position:
                return curr

            counter += 1
            curr = curr.next
        

        return None

    # insert the node in any position ==> [0...N]  
    def insert_after_postion(self, position, node):
        # find the node before the current position
        curr_node = self.get_nth_node(position)

        if curr_node is None: 
            print('Invalid Position') 
            return

        # update the link of the new node with previous node link
        node.next = curr_node.next
        # update previous node link with new node link
        curr_node.next = node

        return node


    # delete node at any position ==> [0...N]  
    def delete_node_with_position(self, pos):
        curr = self.head
        # check list has head node
        if curr is None:
            return None
       
        if pos == 0:
            # delete the head node at position 0
            new_head = curr.next
            while True:
                if curr.next is self.head:
                    break
                curr = curr.next

            curr.next = new_head
            
            temp = self.head.data
            # free memory for the prev head node
            del self.head.data

            # make the head link as new head
            self.head = new_head

            return str(temp) if temp == 0 else temp
        
        # if the posistion is not at the head 
        # find the position bw intermediate node to tail node
        prev = curr
        counter = 0
        while True:
            if curr.next is self.head:
                if counter < pos:
                    return None

            if counter == pos:
                break

            counter += 1
            prev = curr
            curr = curr.next

        # unlink the link bw previous node to current node
        prev.next = curr.next

        # return the deleted node data 
        return_node_data = curr.data
        
        # free memory for the given positional node data  
        del curr.data

        return return_node_data





if __name__ == '__main__':


    head = Node(data=1)
    llist = LinkedList()
    print('Make as Head Node : ', head.data)
    llist.make_head(head)

    node_two = Node(data=2)
    llist.append_node(node_two)
    node_three = Node(data=3)
    llist.append_node(node_three)
    node_four = Node(data=4)
    llist.append_node(node_four)

    node_zero = Node(data=0)
    print('Update Head with : ', node_zero.data)
    llist.push_head(node_zero)


    new_node = Node(data=100)
    insert_position = 0
    insert_node = llist.insert_after_postion(insert_position, new_node)
    print('Node inserted at after position :', insert_position,' is ',  insert_node.data if insert_node else 'Invalid Position!!' )

    nth_position = 1
    get_nth_node_at = llist.get_nth_node(nth_position)
    print("Node at nth :",nth_position ,' is ', get_nth_node_at.data if get_nth_node_at else 'Invalid Position!!' )


    llist_length = llist.list_length()
    print('Total length of the list is :', llist_length)

    llist_length_rec = llist.list_len_rec(llist.head)
    print('Total length of the list in (recursively) :', llist_length_rec)


    deleted_position = 0
    delete_node_in_pos = llist.delete_node_with_position(deleted_position)
    print('Node deleted in the list at posistion :', deleted_position,' is ', delete_node_in_pos if delete_node_in_pos else 'Invalid Position!!')

    print('Print Linked list :')
    llist.traverse_list()



