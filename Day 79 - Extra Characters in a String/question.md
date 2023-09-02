# Question

[Link](https://leetcode.com/problems/extra-characters-in-a-string/description/)

You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s optimally.

 

Example 1:

    Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
    Output: 1
    Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.

Example 2:

    Input: s = "sayhelloworld", dictionary = ["hello","world"]
    Output: 3
    Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.

 

Constraints:

    1 <= s.length <= 50
    1 <= dictionary.length <= 50
    1 <= dictionary[i].length <= 50
    dictionary[i] and s consists of only lowercase English letters
    dictionary contains distinct words

# Solution

Runtime : 255ms (beats 5.14%)
Memory : 44.68mb (beats 8.57%)

```java
class Solution {
    Map<String, Integer> dp;

    public Solution(){
        dp = new HashMap<>();
    }

    public boolean checkStringExists(String s, String[] dictionary){
        for(int i=0; i<dictionary.length; i++) if(dictionary[i].equals(s)) return true;
        return false;
    }

    public int minExtraCharRecursive(String s, String[] dictionary){
        if(s.equals("")) return 0;

        if(dp.containsKey(s)) return dp.get(s);

        int minExtraChars = Integer.MAX_VALUE;
        for(int i=0; i<s.length(); i++){
            String right = s.substring(i+1);
            String left = s.substring(0, i+1);
            int curr = checkStringExists(left, dictionary) ? 0 : left.length();
            curr += minExtraCharRecursive(right, dictionary);
            //System.out.println(right+ " // " + left + " //" +  curr);
            minExtraChars = minExtraChars < curr ? minExtraChars : curr;
        }
        dp.put(s, minExtraChars);
        return minExtraChars;
    }
    
    public int minExtraChar(String s, String[] dictionary) {
        return minExtraCharRecursive(s, dictionary);
    }
}
```

If you understand the problem, you realize that we have to consider all combinations of substrings. And if we do this brute force, we will have to consider all possible combinations of substrings. This is exponential time complexity. So we need to optimize it. At this point dp comes to mind. We can use dp to iterate all combinations of substrings only once. We can use a map to store the minimum extra characters for a given string. We can then use this map to avoid calculating the same string again.

In this solution, we split given string into two parts, left and right. We check if left part is present in dictionary. If it is, we don't need to add any extra characters. If it is not, we need to add all the characters in left part. We then recursively call the function on right part. We do this for all possible splits and return the minimum value.