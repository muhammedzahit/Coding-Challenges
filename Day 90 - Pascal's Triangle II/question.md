# Question

[Link](https://leetcode.com/problems/pascals-triangle-ii/description/)

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

![Alt text](PascalTriangleAnimated2.gif)

Example 1:

    Input: rowIndex = 3
    Output: [1,3,3,1]

Example 2:

    Input: rowIndex = 0
    Output: [1]

Example 3:

    Input: rowIndex = 1
    Output: [1,1]

Constraints:

    0 <= rowIndex <= 33

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

# Solution

Runtime : 1ms

```java
class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> res = new ArrayList<>();
        res.add(1);
        if(rowIndex == 0) return res;
        res.add(1);
        if(rowIndex == 1) return res;
        for(int i=3; i<=rowIndex+1; i++){
            for(int j=i-2; j>0; j--) res.set(j, res.get(j) + res.get(j-1));
            res.add(1);
        }
        return res;
    }
}
```

In this solution we will grow the list in each row. And we will iterate from i-1 to 1 and add the value of the previous index to the current index. And we will add 1 at the end of the list. We will do this for rowIndex+1 times. And we will return the list. Like this we can achieve O(rowIndex) space complexity.