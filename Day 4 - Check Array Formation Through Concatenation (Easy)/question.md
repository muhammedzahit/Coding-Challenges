# Question

You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].

Return true if it is possible to form the array arr from pieces. Otherwise, return false.

Example 1:

Input: arr = [15,88], pieces = [[88],[15]]
Output: true
Explanation: Concatenate [15] then [88]

Example 2:

Input: arr = [49,18,16], pieces = [[16,18,49]]
Output: false
Explanation: Even though the numbers match, we cannot reorder pieces[0].

Example 3:

Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
Output: true
Explanation: Concatenate [91] then [4,64] then [78]

 

Constraints:

    1 <= pieces.length <= arr.length <= 100
    sum(pieces[i].length) == arr.length
    1 <= pieces[i].length <= arr.length
    1 <= arr[i], pieces[i][j] <= 100
    The integers in arr are distinct.
    The integers in pieces are distinct (i.e., If we flatten pieces in a 1D array, all the integers in this array are distinct).

# Solution

0 ms
```java
class Solution {
    public boolean canFormArray(int[] arr, int[][] pieces) {
        int i = 0;
        while(i < arr.length){
            boolean found = false;
            for(int j=0; j<pieces.length; j++){
                if(arr[i] == pieces[j][0]){
                    for(int k=1; k<pieces[j].length; k++){
                        if(arr[i+k] != pieces[j][k]) return false;
                    }  
                    found = true;
                    i += pieces[j].length;
                    break;
                }
            }
            if(!found) return false;
        }
        return true;
    }
}
```

We are looking for matched patterns from pieces in arr. So we can use a while loop to iterate arr, and use a for loop to iterate pieces. If we find a matched pattern, we can move i to the next position of the pattern. If we cannot find a matched pattern, we can return false.