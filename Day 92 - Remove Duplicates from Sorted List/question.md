# Question

[Link](https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/)

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:

![Alt text](list1.jpg)

    Input: head = [1,1,2]
    Output: [1,2]

Example 2:

![Alt text](list2.jpg)

    Input: head = [1,1,2,3,3]
    Output: [1,2,3]

Constraints:

    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.

# Solution

Runtime : 0 ms

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        // list guarenteed to be ascending order
        if(head == null || head.next == null) return head;
        ListNode temp = head.next;
        ListNode before = head;
        while(true){
            if(temp == null) break;
            if(temp.val == before.val){
                temp = temp.next;
                before.next = temp;
            }
            else{
                before = temp;
                temp = temp.next;
            }
        }
        return head;
        
    }
}
```

In this solution, we use two pointers to traverse the list. One pointer is the current node, and the other is the node before the current node. If the current node's value is equal to the node before it, we change the node before it's next pointer to the current node's next pointer. Thus we delete the current node. If the current node's value is not equal to the node before it, we move both pointers to the next node. We repeat this process until the current node is null.