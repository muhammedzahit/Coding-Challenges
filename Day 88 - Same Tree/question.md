# Question

[Link](https://leetcode.com/problems/same-tree/description/)

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:

![Alt text](ex1.jpg)

    Input: p = [1,2,3], q = [1,2,3]
    Output: true

Example 2:

![Alt text](ex2.jpg)

    Input: p = [1,2], q = [1,null,2]
    Output: false

Example 3:

![Alt text](ex3.jpg)

    Input: p = [1,2,1], q = [1,1,2]
    Output: false

Constraints:

    The number of nodes in both trees is in the range [0, 100].
    -104 <= Node.val <= 104

# Solution

Runtime : 0 ms

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        Stack<TreeNode> stack = new Stack<>();
        if(p == null || q == null){
            if(p == null && q == null) return true;
            return false;
        }
        if(p.val != q.val) return false;
        stack.push(p);
        stack.push(q);
        while(!stack.empty()){
            TreeNode child_q = stack.pop();
            TreeNode child_p = stack.pop();
            if( (child_q.left != null && child_p.left == null) || (child_q.left == null && child_p.left != null) ) return false;
            if( (child_q.right != null && child_p.right == null) || (child_q.right == null && child_p.right != null) ) return false;
            if(child_q.left != null){
                if(child_q.left.val != child_p.left.val) return false;
                stack.push(child_p.left);
                stack.push(child_q.left);
            }
            if(child_q.right != null){
                if(child_q.right.val != child_p.right.val) return false;
                stack.push(child_p.right);
                stack.push(child_q.right);
            }
        }
        return true;
    }
}
```

In this solution We used stack traversal method to traverse both trees at the same time. We used a stack to store the nodes of both trees. We checked every node of both trees at the same time. If the value of both nodes are not equal then we return false. If the value of both nodes are equal then we check if the left child of both nodes are null or not. If one of them is null and the other is not null then we return false. If both of them are not null then we check if the value of both left child are equal or not. If they are not equal then we return false. If they are equal then we push both left child into the stack. We do the same thing for the right child. If we can traverse both trees completely then we return true.