# Question

[Link](https://leetcode.com/problems/longest-common-prefix/description/)

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

    Input: strs = ["flower","flow","flight"]
    Output: "fl"

Example 2:

    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.

# Solution

Runtime : 14 ms

```java
class Solution {
    public String findLongestPrefixBetween(String left, String right){
        int i=0;
        String prefix = "";
        while(i < left.length() && i < right.length()){
            if(left.charAt(i) == right.charAt(i)) prefix += right.charAt(i);
            else break;
            i += 1;
        }
        return prefix;
    }

    public String longestCommonPrefix(String[] strs) {
        String longestPrefix = strs[0];
        for(int i=1; i < strs.length; i++){
            longestPrefix = findLongestPrefixBetween(longestPrefix, strs[i]);
        }
        return longestPrefix;
    }
}
```

In this solution we are iterating over the array of strings and finding the longest common prefix between the current longest prefix and the current string. This is done by iterating over the characters of the two strings and appending the character to the prefix if the characters are same. If the characters are not same, we break out of the loop and return the prefix. This is done for all the strings in the array and the final prefix is returned.