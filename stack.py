# https://www.geeksforgeeks.og/stack-in-python/

class Node:
    def __init__(self, value):
        super().__init__()
        self.value = value
        self.next = None



class Stack:
    def __init__(self, ):
        super().__init__()
        self.head = None
        self.size = 0

    def __str__(self):
        if self.empty_stack():
            raise Exception('Empty stack!')

        curr = self.head   
        out = '' 
        while curr:
            out += str(curr.value) + "->"
            curr = curr.next
        
        return out[:-3]

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
        
        return self.head.next.value

    def push(self, node):
        if self.empty_stack():
            raise Exception('Empty stack!')
        pass

    def pop(self, ):
        if self.empty_stack():
            raise Exception('Empty stack!')
        pass


if __name__ == "__main__":
    stack = Stack()
    stack_head = Node('Head')
    stack.set_stack_head(stack_head)

    stack.set_stack_head(Node('dupe'))

    # stack.peek()



