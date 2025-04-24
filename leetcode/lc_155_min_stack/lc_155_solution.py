class MinStack:
    def __init__(self):
        # Initialize the main stack to store all elements
        self.stack = []
        # Initialize the min stack to store the minimum element at each stage
        self.minStack = []

    def push(self, val: int) -> None:
        # Always push the new value onto the main stack
        self.stack.append(val)

        # If the minStack is not empty, compare the new value with the current minimum
        if self.minStack:
            # The new minimum is the smaller of the current minimum and the new value
            minVal = min(self.minStack[-1], val)
            # Push the new minimum onto the minStack
            self.minStack.append(minVal)
        else:
            # If the minStack is empty, the first element is the minimum
            self.minStack.append(val)

    def pop(self) -> None:
        # Ensure both stacks are non-empty before attempting to pop
        if self.stack and self.minStack:
            # Pop the top element from the main stack
            self.stack.pop()
            # Pop the top element from the minStack (corresponding to the popped element)
            self.minStack.pop()

    def top(self) -> int:
        # If the main stack is not empty, return the top element
        if self.stack:
            return self.stack[-1]
        # If the stack is empty, return None
        return None

    def getMin(self) -> int:
        # If the minStack is not empty, the top element is the current minimum
        if self.stack and self.minStack:
            return self.minStack[-1]
        # If the stack is empty, return None
        return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()