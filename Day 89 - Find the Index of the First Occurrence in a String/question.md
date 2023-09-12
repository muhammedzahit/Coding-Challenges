# Question

[Link](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/)

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

    Input: haystack = "sadbutsad", needle = "sad"
    Output: 0
    Explanation: "sad" occurs at index 0 and 6.
    The first occurrence is at index 0, so we return 0.

Example 2:

    Input: haystack = "leetcode", needle = "leeto"
    Output: -1
    Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:

    1 <= haystack.length, needle.length <= 104
    haystack and needle consist of only lowercase English characters.

# Solution

Runtime : 1ms

```java
class Solution {
    public int strStr(String haystack, String needle) {
        int needle_index = 0;
        for(int i=0; i<haystack.length(); i++){
            if(haystack.charAt(i) == needle.charAt(needle_index)){
                int j = i+1;
                needle_index++;
                while(j < haystack.length() && needle_index < needle.length() && haystack.charAt(j) == needle.charAt(needle_index)){
                    needle_index++;
                    j++;
                }
                if(needle_index == needle.length()) return  i;
                needle_index = 0;
            }
        }
        return -1;
    }
}
```

In this solution, we iterate through the haystack and check if the current character matches the first character of the needle. If it does, we iterate through the needle and check if the characters match. If they do, we return the index of the haystack. If they don't, we reset the needle_index and continue iterating through the haystack. If we reach the end of the haystack and haven't found a match, we return -1.