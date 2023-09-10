# Question

[Link](https://leetcode.com/problems/binary-tree-inorder-traversal/description/)

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:

    Input: root = [1,null,2,3]
    Output: [1,3,2]

Example 2:

    Input: root = []
    Output: []

Example 3:

    Input: root = [1]
    Output: [1]

Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

 
Follow up: Recursive solution is trivial, could you do it iteratively?

# Solution

Runtime : 1ms

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
    public List<Integer> inorderTraversal(TreeNode root) {
        Stack<TreeNode> stackList = new Stack<>();
        Map<TreeNode, Boolean> checkList = new HashMap<>();
        List<Integer> res = new ArrayList<>();
        stackList.add(root);
        while(!stackList.empty()){
            TreeNode temp = stackList.pop();
            if(temp == null) continue;
            else if(checkList.containsKey(temp)) res.add(temp.val);
            else if(temp.left == null && temp.right == null) res.add(temp.val);
            else{
                if(temp.left != null) stackList.add(temp.left);
                stackList.add(temp);
                if(temp.right != null) stackList.add(temp.right);
            }
            checkList.put(temp, true);
        }
        Collections.reverse(res);
        return res;
    }
}
```

In this solution, I used a stack to store the nodes. I also used a hashmap to keep track of the nodes that have been visited. If a node has been visited, it is added to the result list. If a node has not been visited, it is added to the stack. If a node has a left child, it is added to the stack. If a node has a right child, it is added to the stack. If a node has no children, it is added to the result list. The result list is then reversed and returned.