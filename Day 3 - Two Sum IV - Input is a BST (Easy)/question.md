# Question

Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

 

Example 1:
![](https://assets.leetcode.com/uploads/2020/09/21/sum_tree_1.jpg)
Input: root = [5,3,6,2,4,null,7], k = 9

Output: true

Example 2:
![](https://assets.leetcode.com/uploads/2020/09/21/sum_tree_2.jpg)
Input: root = [5,3,6,2,4,null,7], k = 28

Output: false

 

Constraints:

    The number of nodes in the tree is in the range [1, 104].
    -104 <= Node.val <= 104
    root is guaranteed to be a valid binary search tree.
    -105 <= k <= 105

# Solution

3 ms

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
    public boolean search(TreeNode root, int num, TreeNode prev){
        if(root == null) return false;
        if(root.val == num && root != prev) return true;
        else if(root.val < num && root.right != null) return search(root.right, num, prev);
        else if(root.val > num && root.left != null) return search(root.left, num, prev);
        return false;
    }
    
    public boolean findTarget(TreeNode root, int k) {
        List<TreeNode> stack = new ArrayList<>();
        stack.add(root);
        while(stack.size() != 0){
            TreeNode current = stack.get(0);
            stack.remove(0);

            if( search(root, k - current.val, current) ) return true;

            if(current.right != null) stack.add(current.right);
            
            if(current.left != null) stack.add(current.left);
        }   

        return false;
    }
}
```

We will traverse binary tree by stack data structure and look for node that have value when added to the  current value equals k.