# Question

[Link](https://leetcode.com/problems/implement-stack-using-queues/description/)

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

    void push(int x) Pushes element x to the top of the stack.
    int pop() Removes the element on the top of the stack and returns it.
    int top() Returns the element on the top of the stack.
    boolean empty() Returns true if the stack is empty, false otherwise.

Notes:

    You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
    Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

Example 1:

    Input
    ["MyStack", "push", "push", "top", "pop", "empty"]
    [[], [1], [2], [], [], []]
    Output
    [null, null, null, 2, 2, false]

    Explanation
    MyStack myStack = new MyStack();
    myStack.push(1);
    myStack.push(2);
    myStack.top(); // return 2
    myStack.pop(); // return 2
    myStack.empty(); // return False
 

Constraints:

    1 <= x <= 9
    At most 100 calls will be made to push, pop, top, and empty.
    All the calls to pop and top are valid.

 
Follow-up: Can you implement the stack using only one queue?

# Solution

Runtime : 0 ms

```java
class MyStack {
    private int[] list;
    private int listSize;
    private int limit;

    private void increaseLimit(){
        int[] newList = new int[limit*2];
        for(int i=0; i<limit; i++) newList[i] = this.list[i];
        this.list = newList;
        this.limit *= 2;
    } 

    public MyStack() {
        this.list = new int[2];
        this.limit = 2;
        this.listSize = 0;
    }
    
    public void push(int x) {
        if(this.listSize + 1 == limit) this.increaseLimit();
        this.list[this.listSize] = x;
        this.listSize += 1;
    }
    
    public int pop() {
        if(this.listSize == 0) return Integer.MAX_VALUE;
        this.listSize -= 1;
        return this.list[this.listSize];
    }
    
    public int top() {
        if(this.listSize == 0) return Integer.MAX_VALUE;
        return this.list[this.listSize - 1];
    }
    
    public boolean empty() {
        return this.listSize == 0;
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */
```