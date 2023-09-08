# Question

[Link](https://leetcode.com/problems/pascals-triangle/description)

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

![Alt text](PascalTriangleAnimated2.gif)

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]

Constraints:

    1 <= numRows <= 30

# Solution

Runtime : 1ms

```java
class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> pascal = new ArrayList<>();
        List<Integer> temp = new ArrayList<>(); temp.add(1);
        pascal.add(temp);

        for(int i=1; i<numRows; i++){
            temp = new ArrayList<>(); temp.add(1);
            for(int j=1; j<pascal.get(i-1).size(); j++){
                temp.add(pascal.get(i-1).get(j) + pascal.get(i-1).get(j-1));
            }
            temp.add(1); pascal.add(temp);
        }
        
        return pascal;
    }
}
```

In this solution, we are using the fact that the next row is the sum of the previous row and the previous row shifted by one. We are using a temporary list to store the previous row and then adding the current row to the pascal list.