# make head as new node

class Node:
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.next = None



class Stack:
    def __init__(self):
        super().__init__()
        self.head = None
        self.size = 0
        # set stack head
        self.set_stack_head(Node('Head'))

    def __str__(self):
        if self.empty_stack():
            raise Exception('Empty stack!')

        curr = self.head.next  
        out_list = list()
        while curr:
            out_list.append(curr.data)
            curr = curr.next
        
        return '->'.join([str(i) for i in out_list])

    def set_stack_head(self, node):
        if self.empty_stack() and self.head is None:
            self.head = node
            return True
        raise Exception('Head already set in the stack!')

    def get_size(self, ):
        return self.size

    def empty_stack(self, ):
        return self.size == 0

    def peek(self, ):
        if self.empty_stack():
            raise Exception('Peeking from an empty stack!')
        
        return self.head.next.data

    def push(self, node):
        if self.head is None:
            raise Exception('Empty stack head to push')

        node.next = self.head.next
        self.head.next = node
        self.size += 1
        return True

    def pop(self, ):
        if self.empty_stack():
            raise Exception('Empty stack!')
        
        remove = self.head.next.data
        self.head.next = self.head.next.next
        self.size -= 1
        return remove


if __name__ == "__main__":
    stack = Stack()

    one = Node(10)
    stack.push(one)
    two = Node(20)
    stack.push(two)
    three = Node(30)
    stack.push(three)


    print('stack head ',stack.head.data)

    print('stack elements :', stack)

    print('pop stack top element:', stack.pop())

    print('stack peek(top) element :', stack.peek())

    print('stack size : ', stack.get_size())

    print('stack empty ?', stack.empty_stack())

    print('after operation stack elements :', str(stack))



